#py script is used to combine and organize ECList
#Usage: C:\Windows\System32>D:
cd D:\EClist
python extract_ec_from_keg.py
python extract_ec_from_keg2.py
#Output result: XXECKEGGList.txt

#illustrate:
#extract_ec_from_keg.py: used to extract all characters between "[EC:" and "]" from all .keg files in the EClist folder, if there is "" between "[EC:" and "]" ", replace " " with a newline character so that each extracted character exists on a separate line. After the character extraction of all .keg files is completed, check whether there are duplicate lines, if so, delete the duplicate lines and store the results as ECKEGGList.txt
#extract_ec_from_keg2.py: Used to check the ECKEGGList.txt file, delete lines with "-", then delete duplicate lines, and store them as XXECKEGGList.txt
