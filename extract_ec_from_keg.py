import os

def extract_ec_from_keg(file_path):
    with open(file_path, 'r') as keg_file:
        content = keg_file.read()
        # 使用正则表达式提取 [EC:...] 中的内容
        ec_list = re.findall(r'\[EC:(.*?)\]', content)
        # 将空格替换为换行符
        ec_list = [ec.replace(' ', '\n') for ec in ec_list]
        return ec_list

def main():
    folder_path = 'D:\\Qiang\\NJAU\\ModelConstruction\\EClist'  # EClist 文件夹路径
    output_file = 'ECKEGGList.txt'  # 输出文件名

    all_ecs = set()  # 用于存储所有提取的 EC
    for filename in os.listdir(folder_path):
        if filename.endswith('.keg'):
            file_path = os.path.join(folder_path, filename)
            ecs = extract_ec_from_keg(file_path)
            all_ecs.update(ecs)

    # 将结果写入文件
    with open(output_file, 'w') as output:
        for ec in sorted(all_ecs):
            output.write(ec + '\n')

if __name__ == '__main__':
    import re
    main()
