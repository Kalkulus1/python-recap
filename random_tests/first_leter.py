# Find the first non-repeating character in a string

# Example
## Input: kubyk
## Output: u

## Input: kubuyk
## Output: b

from collections import Counter

def firstLetter(letters):

    dct = dict(Counter(letters))

    print(dct)

    for letter in dct:

        if dct[letter] == 1:

            print(letter)

            break

firstLetter('kubyk')
firstLetter('kubuyk')

def first_letter(s):
    dct = {}

    for letter in s:
        if letter in dct:
            dct[letter] += 1
        else:
            dct[letter] = 1
    
    for letter in dct:
        if dct[letter] == 1:
            print(letter)
            break

first_letter('kubuyk')