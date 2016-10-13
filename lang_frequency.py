import collections
import argparse
import sys
import re
from string import punctuation


parser = argparse.ArgumentParser(description='Top 10 word in text')
parser.add_argument('-file', dest='filepath',
                    help='Input filepath and filename')
args = parser.parse_args()


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print('Файл не найден')
        sys.exit(1)
    except ValueError:
        print('Формат файла не подходит для вывода данных')


def get_most_frequent_words(text):
    count_word = collections.Counter()
    words = re.sub(r'[{}]'.format(punctuation), "", text)
    for word in words.split(' '):
        count_word[word] += 1
    return sorted(count_word.items(), key=lambda x: x[1], reverse=True)[:10]


if __name__ == '__main__':
    data = load_data(args.filepath)
    print(get_most_frequent_words(data))
