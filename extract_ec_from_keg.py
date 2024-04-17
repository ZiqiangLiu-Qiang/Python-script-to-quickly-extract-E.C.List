import os

def extract_ec_from_keg(file_path):
     with open(file_path, 'r') as keg_file:
         content = keg_file.read()
         # Use regular expressions to extract the content in [EC:...]
         ec_list = re.findall(r'\[EC:(.*?)\]', content)
         # Replace spaces with newlines
         ec_list = [ec.replace(' ', '\n') for ec in ec_list]
         returnec_list

def main():
     folder_path = 'D:\\EClist' # EClist folder path
     output_file = 'ECKEGGList.txt' # Output file name

     all_ecs = set() # Used to store all extracted ECs
     for filename in os.listdir(folder_path):
         if filename.endswith('.keg'):
             file_path = os.path.join(folder_path, filename)
             ecs = extract_ec_from_keg(file_path)
             all_ecs.update(ecs)

     #Write results to file
     with open(output_file, 'w') as output:
         for ec in sorted(all_ecs):
             output.write(ec + '\n')

if __name__ == '__main__':
     import re
     main()
