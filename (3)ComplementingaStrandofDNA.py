# Define the file path
file_path = "E:/Python/Rosalind/(3)Complementing_a_Strand_of_DNA.txt"  

# Read the DNA string from the file
with open(file_path, "r") as file:
    dna_string = file.read().strip()

# Create a complement map for DNA
complement = str.maketrans("ATCG", "TAGC")

# Find the reverse complement
reverse_complement = dna_string.translate(complement)[::-1]

# Print the reverse complement
print(reverse_complement)
