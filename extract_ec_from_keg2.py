# Read original file
input_filename = "ECKEGGList.txt"
output_filename = "XXECKEGGList.txt"

# Read file content
with open(input_filename, "r") as infile:
     lines = infile.readlines()

# Remove lines with "-"
filtered_lines = [line for line in lines if "-" not in line]

# Remove duplicate rows
unique_lines = list(set(filtered_lines))

#Write results to new file
with open(output_filename, "w") as outfile:
     outfile.writelines(unique_lines)

print(f"Processing completed, results have been saved to {output_filename}")
