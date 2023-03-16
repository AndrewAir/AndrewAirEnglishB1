import argparse
import random

def extract_words(input_file: str) -> list:
    words = []
    with open(input_file, 'r') as file:
        for line in file:
            if not line.strip().startswith(('#', '>')):
                first_word = line.strip().split()[0]
                words.append(first_word)
    return words

def generate_sequences(words: list, seq_length: int) -> list:
    sequences = []
    for i in range(0, len(words), seq_length):
        seq = words[i:i + seq_length]
        if len(seq) == seq_length:
            sequences.append(seq)
    return sequences

def generate_random_sequence(sequences: list, total_length: int) -> str:
    random_seq = []
    for _ in range(total_length):
        seq = random.choice(sequences)
        word = random.choice(seq)
        random_seq.append(word)
    return ' '.join(random_seq)

def main():
    parser = argparse.ArgumentParser(description='Generate touch typing practice text from input file.')
    parser.add_argument('input_file', type=str, help='Path to the input text file.')
    parser.add_argument('-o', '--output_file', type=str, default='FileNameTouchTypingPractice.txt', help='Path to the output text file.')
    args = parser.parse_args()

    words = extract_words(args.input_file)
    sequences = generate_sequences(words, 10)
    random_sequence = generate_random_sequence(sequences, 100)

    with open(args.output_file, 'w') as file:
        file.write(random_sequence)

if __name__ == '__main__':
    main()
