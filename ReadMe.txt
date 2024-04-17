#py脚本用于ECList的组合和整理
#使用：		C:\Windows\System32>D:
			cd D:\EClist
			python extract_ec_from_keg.py
			python extract_ec_from_keg2.py
#输出结果：XXECKEGGList.txt

#说明：
#extract_ec_from_keg.py：用于将EClist文件夹内的所有.keg文件中，提取“[EC:”和“]”之间的所有字符，如果在“[EC:”和“]”之间存在“ ”，则将“ ”替换为换行符，使得每一个所提取的字符单独存在于一行。当完成所有.keg文件的字符提取后，检查是否有重复的行，如果有则将重复的行删除，并将结果存储为ECKEGGList.txt
#extract_ec_from_keg2.py：用于检查ECKEGGList.txt文件，删除带有“-”的行，然后删除重复行，并储存为XXECKEGGList.txt
