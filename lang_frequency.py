import collections
import argparse
import sys


parser = argparse.ArgumentParser(description='Pretty print for JSON')
parser.add_argument('-file', dest='filepath',
                    help='Input filepath and filename with expansion json' )
args = parser.parse_args()


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as f:
            return f.read()
    except (FileNotFoundError):
        print('Файл не найден')
        sys.exit(1)


def get_most_frequent_words(text):
    count_word = collections.Counter()
    for word in text.split():
        count_word[word] += 1
    return count_word



if __name__ == '__main__':
    data = load_data(args.filepath)
    print(get_most_frequent_words(data))
