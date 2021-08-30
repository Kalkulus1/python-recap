from collections import Counter

def firstLetter(letters):

    dct = dict(Counter(letters))

    print(dct)

    for letter in dct:

        if dct[letter] == 1:

            print(letter)

            break

firstLetter('kubyk')