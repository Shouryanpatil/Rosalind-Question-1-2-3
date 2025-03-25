# Define the file path
file_path = "E:/Python/Rosalind/(1)Counting_DNA_Nucleotides.txt"  

# Read the DNA string from the file
with open(file_path, "r") as file:
    dna_string = file.read().strip()

# Count the occurrences of each nucleotide
count_A = dna_string.count('A')
count_C = dna_string.count('C')
count_G = dna_string.count('G')
count_T = dna_string.count('T')

# Print the results
print(count_A, count_C, count_G, count_T)