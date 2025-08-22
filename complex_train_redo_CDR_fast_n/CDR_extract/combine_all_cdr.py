import pandas as pd
import glob

# 定义文件路径
file_pattern = '*_antibody_CDR.txt'  # 替换为实际的文件路径

# 获取所有匹配的文件
files = glob.glob(file_pattern)

# 读取每个文件并合并到一个 DataFrame 中
combined_df = pd.concat([pd.read_csv(f, sep=',') for f in files], ignore_index=True)

# 查看合并后的 DataFrame
print(combined_df)

# 输出文件路径
output_file = 'combined_sequences.txt'

# 保存到文件
combined_df.to_csv(output_file, index=False)

print(f"合并后的结果已保存到 {output_file}")


