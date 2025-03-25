# Define the file path
file_path = "E:/Python/Rosalind/(2)Transcribing_DNA_into_RNA.txt"  

# Read the DNA string from the file
with open(file_path, "r") as file:
    dna_string = file.read().strip()

# Replace all occurrences of 'T' with 'U' to transcribe RNA
rna_string = dna_string.replace('T', 'U')

# Print the transcribed RNA string
print(rna_string)