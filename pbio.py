"""
FASTA Sequence Generator
Purpose: Generates random DNA sequences in FASTA format with user-specified parameters,
         inserts the user's name at a random position, and calculates sequence statistics.
Context: Bioinformatics tool for creating test sequences while maintaining proper FASTA format.
"""

import random

def generate_dna_sequence(length):
    """Generate random DNA sequence of given length using A, C, G, T nucleotides."""
    # ORIGINAL:
    # return ''.join(random.choices(['A', 'C', 'G', 'T'], weights=None, k=length))
    # MODIFIED (more efficient for large sequences and clearer nucleotide selection):
    nucleotides = ['A', 'C', 'G', 'T']
    return ''.join(random.choice(nucleotides) for _ in range(length))

def insert_name(sequence, name):
    """Insert name at random position in sequence without affecting statistics."""
    if len(sequence) == 0:
        return name
    
    # ORIGINAL:
    # pos = random.randint(0, len(sequence))
    # return sequence[:pos] + name + sequence[pos:]
    # MODIFIED (better variable names and handles edge cases):
    insert_position = random.randint(0, len(sequence))
    return f"{sequence[:insert_position]}{name}{sequence[insert_position:]}"

def calculate_statistics(sequence):
    """Calculate nucleotide percentages and CG ratio in the DNA sequence."""
    total = len(sequence)
    if total == 0:
        return {'A': 0, 'C': 0, 'G': 0, 'T': 0, 'CG': 0}
    
    counts = {
        'A': sequence.count('A'),
        'C': sequence.count('C'),
        'G': sequence.count('G'),
        'T': sequence.count('T')
    }
    
    return {
        'A': (counts['A'] / total) * 100,
        'C': (counts['C'] / total) * 100,
        'G': (counts['G'] / total) * 100,
        'T': (counts['T'] / total) * 100,
        'CG': ((counts['C'] + counts['G']) / total) * 100
    }

def save_fasta_file(seq_id, description, sequence):
    """Save sequence to FASTA file with proper formatting."""
    filename = f"{seq_id}.fasta"
    with open(filename, 'w') as fasta_file:
        fasta_file.write(f">{seq_id} {description}\n{sequence}\n")
    return filename

def validate_sequence_length(input_str):
    """Validate that sequence length is a positive integer."""
    # ORIGINAL:
    # return int(input_str)
    # MODIFIED (proper validation with error messages):
    try:
        length = int(input_str)
        if length <= 0:
            raise ValueError("Length must be positive")
        return length
    except ValueError:
        raise ValueError("Please enter a valid positive integer")

def main():
    print("FASTA DNA Sequence Generator")
    print("---------------------------")
    
    try:
        # Get user input
        length = validate_sequence_length(input("Enter the sequence length: "))
        seq_id = input("Enter the sequence ID: ").strip()
        description = input("Provide a description of the sequence: ").strip()
        name = input("Enter your name: ").strip()
        
        # Generate and process sequence
        dna_sequence = generate_dna_sequence(length)
        stats = calculate_statistics(dna_sequence)
        final_sequence = insert_name(dna_sequence, name)
        
        # Save to FASTA file
        filename = save_fasta_file(seq_id, description, final_sequence)
        
        # Display results
        print(f"\nThe sequence was saved to the file {filename}")
        print("Sequence statistics (excluding your name):")
        print(f"A: {stats['A']:.1f}%")
        print(f"C: {stats['C']:.1f}%") 
        print(f"G: {stats['G']:.1f}%")
        print(f"T: {stats['T']:.1f}%")
        print(f"CG content: {stats['CG']:.1f}%")
        
    except Exception as e:
        print(f"\nError: {e}")
        print("Please restart the program with valid inputs.")

if __name__ == "__main__":
    main()