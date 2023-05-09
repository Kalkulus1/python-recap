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




def anagramTest(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False
    
    # Check count for each letter
    count = {}
    
    # check letter in count
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    print(count)

    for k in count:
        print(f"{k} -- {count[k]}")
        if count[k] != 0:
            return False
    return True
    
print(anagramTest('dog god', 'god doG'))