import pandas as pd

file_path = 'all_data/combined_sequences.txt'  # 替换成你的文件路径
df = pd.read_csv(file_path)

# 将 DataFrame 转换为字典
sequences_dict = df.set_index('name')['combined_sequence'].to_dict()

# 打印字典
print(sequences_dict)

