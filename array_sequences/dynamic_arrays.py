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
    # return sorted(s1) == sorted(s2)

print(anagram('dog god', 'god doG'))
print(anagram2('dog god', 'god doG'))