import random

english = open('english.txt')
wordslist = {}
words = int(input('Enter the number of words for your password: '))

for line in english:
    number, word = line.split()
    wordslist[int(number)] = word
english.close()

while words > 0:
    x = random.randint(11111, 66666)
    if '0' in str(x):
        words = words
    elif '7' in str(x):
        words = words
    elif '8' in str(x):
        words = words
    elif '9' in str(x):
        words = words
    else:
        print(wordslist[x])
        words -= 1
