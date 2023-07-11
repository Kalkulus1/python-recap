def anagram2(s1, s2):
    
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)

def anagram(s1, s2):

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Check if they have the same letters
    if len(s1) != len(s2):
        return False

    # count frequency of each letter
    count = {}

    # Add to count
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    # Reverser
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    for k in count:
        if count[k] != 0:
            print("Not Zero")
            return False
    
    return True

print(anagram('dog god', 'god doG'))




def anagramTest(s1: str, s2: str):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

    if len(s1) != len(s2):
        return False
    
    count = {}

    for char in s1:
        count[char] = count.get(char, 0) + 1
    print(count)
    
    for char in s2:
        count[char] = count.get(char, 0) - 1
    
    print(count)

    for k in count:
        if count[k] != 0:
            return False
    
    return True

print(anagramTest('dog god', 'god doG'))

from collections import Counter

def anagramTest2(s1, s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

    if len(s1) != len(s2):
        return False

    count_s1 = Counter(s1)
    count_s2 = Counter(s2)

    if count_s1 != count_s2:
        return False
    return True

# print(anagramTest2('dog god', 'god doG'))