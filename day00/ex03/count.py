#!/usr/bin/env python3


import sys
import string


def text_analyzer(*args):
    """This function counts the number of upper characters, lower characters,punctuation and spaces in a given text."""
    if len(args) is not 1 or 0:
        return print("ERROR")
    if len(args) is 0:
        args[0] = input("What is the text to analyse?\n")
    params = {'characters': 0, 'upper': 0, 'lower': 0,'punctuation': 0,'spaces': 0}
    for x in args[0]:
        params['characters'] += 1
        if x.isupper():
            params['upper'] += 1
        if x.islower():
            params['lower'] += 1
        if x in string.punctuation:
            params['punctuation'] += 1
        if x.isspace():
            params['spaces'] += 1
    print('The text contains ' + str(params['characters']) + ' characters:')
    print('- ' + str(params['upper']) + ' upper letters')
    print('- ' + str(params['lower']) + ' lower letters')
    print('- ' + str(params['punctuation']) + ' punctuation marks')
    print('- ' + str(params['spaces']) + ' spaces')

def main():
    text_analyzer()


if __name__ == '__main__':
    main()
