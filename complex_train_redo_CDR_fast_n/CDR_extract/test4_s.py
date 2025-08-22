from anarci import anarci, number
from Bio import SeqIO
from anarci import anarci, number
import os
import sys
# 读取 FASTA 文件
fasta_file = sys.argv[1]
output_f=fasta_file.replace('.fasta','_CDR.txt')
sequences = []
# 解析 FASTA 文件并构建 sequences 列表
for record in SeqIO.parse(fasta_file, "fasta"):
    id = record.id
    seq = str(record.seq)
    sequences.append((id, seq))
# Hand the list of sequences to the anarci function. Number them with the IMGT scheme
results = anarci(sequences, scheme="imgt", output=False)

# Unpack the results. We get three lists
numbering, alignment_details, hit_tables = results

# Each has the same number of elements as the number of sequences submitted
assert len(numbering) == len(alignment_details) == len(hit_tables) == len(sequences)
# Iterate over the sequences
all_cdr_regions=[]
cdr_regions = {}
for i in range(len(sequences)):
    if numbering[i] is None:
        print('ANARCI did not number', sequences[i][0])
    else:
        print('ANARCI numbered', sequences[i][0])
        print('It identified %d domain(s)' % len(numbering[i]))

        # Iterate over the domains
        for j in range(len(numbering[i])):
            domain_numbering, start_index, end_index = numbering[i][j]

            # Extract CDR regions using IMGT scheme
            cdr_positions = {
                'CDR1': (27, 38),
                'CDR2': (56, 65),
                'CDR3': (105, 117)
            }

            #cdr_regions = {}
            for cdr, (start, end) in cdr_positions.items():
                cdr_sequence = ''.join([domain_numbering[k][1] for k in range(start, end + 1) if domain_numbering[k] is not None])
                cdr_regions[cdr+sequences[i][0]] = cdr_sequence.replace('-','')

            print('Extracted CDR regions:')
            for cdr, seq in cdr_regions.items():
                print(f"{cdr}: {seq}")

    print('\n', '_' * 40)

all_cdr_regions.append(cdr_regions)
#print (cdr_regions)
import pandas as pd

#print (all_cdr_regions)
# 将列表转换为 DataFrame
combined_df = pd.DataFrame(all_cdr_regions)

#print (combined_df)
# 将 NaN 值替换为空字符串
combined_df = combined_df.fillna("")

# 定义固定的列名
new_columns = [
    'cdr1_aa_heavy', 'cdr2_aa_heavy', 'cdr3_aa_heavy'
]

# 强行更改列名
combined_df.columns = new_columns

# 打印更改列名后的 combined_df
print(combined_df)

# 截断或填充序列以达到固定的长度
fixed_lengths = {
    'cdr1_aa_heavy': 10,
    'cdr2_aa_heavy': 10,
    'cdr3_aa_heavy': 25
}


for col, length in fixed_lengths.items():
    print (col,combined_df[col])
    combined_df[col] = combined_df[col].apply(lambda seq: seq[:length].ljust(length, 'X'))

# 组合序列并用 "XXXX" 分隔
combined_df['combined_sequence'] = combined_df[new_columns].apply(lambda row: 'X'.join(row), axis=1)

combined_df['combined_sequence'] = combined_df['combined_sequence'].apply(lambda seq: seq.ljust(95, 'X'))

# 显示结果
print(combined_df['combined_sequence'])

combined_df['name'] = [output_f]
# 如果需要，可以将结果保存到新的文件中
combined_df[['name','combined_sequence']].to_csv(output_f, index=False)

