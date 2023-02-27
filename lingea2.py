import sys
import re


def main():
    words = sys.argv[1:]
    sentences = []
    while True:
        try:
            sentence = input()
        except EOFError:
            break
        sentences.append(sentence)
    filter_sentences(words, sentences)


def filter_sentences(words, sentences):
    for i, sentence in enumerate(sentences):
        printed = False
        for word in words:
            if re.search(r'\b' + word.lower() + r'\b', sentence.lower()) \
                    is not None:
                print(sentence)
                printed = True
                break
        if not printed:
            print(str(i + 1) + " " + sentence, file=sys.stderr)


if __name__ == "__main__":
    main()
