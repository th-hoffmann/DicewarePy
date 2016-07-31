#!/usr/bin/env python3

import random

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
