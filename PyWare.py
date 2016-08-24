#!/usr/bin/env python3
# coding: utf-8

import random


def english():
    english = open('english.txt')
    wordslist = {}
    words = int(input('Enter the number of words for your password: '))

    for line in english:
        number, word = line.split()
        wordslist[int(number)] = word
    english.close()

    while words > 0:
        dices = 5
        index = ''
        while dices > 0:
            dice = random.randint(1, 6)
            index += str(dice)
            dices -= 1
        words -= 1
        print(wordslist[int(index)])



def spanish():
    spanish = open('spanish.txt')
    wordslist = {}
    words = int(input('Enter the number of words for your password: '))

    for line in spanish:
        number, word = line.split()
        wordslist[int(number)] = word
    spanish.close()

    while words > 0:
        dices = 5
        index = ''
        while dices > 0:
            dice = random.randint(1, 6)
            index += str(dice)
            dices -= 1
        words -= 1
        print(wordslist[int(index)])



def main():

    print('''

          8888888b.           888       888
          888   Y88b          888   o   888
          888    888          888  d8b  888
          888   d88P 888  888 888 d888b 888  8888b.  888d888 .d88b.
          8888888P"  888  888 888d88888b888     "88b 888P"  d8P  Y8b
          888        888  888 88888P Y88888 .d888888 888    88888888
          888        Y88b 888 8888P   Y8888 888  888 888    Y8b.
          888         "Y88888 888P     Y888 "Y888888 888     "Y8888
                          888
                     Y8b d88P
                      "Y88P"


    1. English
    2. Español
    0. Exit
    ''')

    language = int(input("Select the language: "))

    if language == 1:
        english()
    elif language == 2:
        spanish()
    elif language == 0:
        print("Goodbye!!!")
    else:
        print("Invalid option!")
        main()



if __name__ == "__main__":
    main()
