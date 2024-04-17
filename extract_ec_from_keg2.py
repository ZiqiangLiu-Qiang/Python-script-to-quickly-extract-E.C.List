# 读取原始文件
input_filename = "ECKEGGList.txt"
output_filename = "XXECKEGGList.txt"

# 读取文件内容
with open(input_filename, "r") as infile:
    lines = infile.readlines()

# 去除带有“-”的行
filtered_lines = [line for line in lines if "-" not in line]

# 去除重复行
unique_lines = list(set(filtered_lines))

# 将结果写入新文件
with open(output_filename, "w") as outfile:
    outfile.writelines(unique_lines)

print(f"处理完成，结果已保存到 {output_filename}")
