import argparse
import csv
import os
from collections import Counter
from typing import Dict

def count_words(text: str) -> Dict[str, int]:
    words = text.lower().split()
    return Counter(words)

def update_global_word_count(global_word_count: Dict[str, int], local_word_count: Dict[str, int]):
    for word, count in local_word_count.items():
        if word in global_word_count:
            global_word_count[word] += count
        else:
            global_word_count[word] = count

def write_csv(output_file: str, local_word_count: Dict[str, int], text: str):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['word_count', 'text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'word_count': sum(local_word_count.values()), 'text': text})

def write_global_csv(global_word_count: Dict[str, int], wc: int):
    sorted_words = sorted(global_word_count.items(), key=lambda x: x[1], reverse=True)
    with open('GlobalWordsCount.csv', 'w', newline='') as csvfile:
        fieldnames = ['word', 'total', 'is_learned']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i, (word, count) in enumerate(sorted_words):
            if i >= wc:
                break
            writer.writerow({'word': word, 'total': count, 'is_learned': False})

def main():
    parser = argparse.ArgumentParser(description='Word counter for text files.')
    parser.add_argument('input_file', type=str, help='Path to the input text file.')
    parser.add_argument('-o', '--output_file', type=str, default='output.csv', help='Path to the output CSV file.')
    parser.add_argument('-wc', '--word_count', type=int, default=10, help='Number of new words to show in the global CSV.')
    args = parser.parse_args()

    with open(args.input_file, 'r') as file:
        text = file.read()

    local_word_count = count_words(text)
    write_csv(args.output_file, local_word_count, text)

    global_word_count = {}
    if os.path.exists('GlobalWordsCount.csv'):
        with open('GlobalWordsCount.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                global_word_count[row['word']] = int(row['total'])

    update_global_word_count(global_word_count, local_word_count)
    write_global_csv(global_word_count, args.word_count)

if __name__ == '__main__':
    main()

