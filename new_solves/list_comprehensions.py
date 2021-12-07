
numbers = [4, 2, 1, 6, 9, 7]
# print([x*x for x in numbers])

# print([x for x in numbers if x%2 != 0])


# Vowels
from collections import Counter
sentence = "Returns the result of dividing two numbers"
vowels = {vowel for vowel in sentence if vowel in "aeiou"}
print(vowels)
sentence = 'The rocket, who was named Ted, came back from Mars because he missed his friends.'
# print([cons for cons in sentence if cons not in "aeiou"])

print([x for x in numbers if bool(x % 2)])

print(f"{1 / 3:.2f}")


import random
all_words = "all the words in the world".split()
def get_random_word():
   return random.choice(all_words)


student_grades = {}
grades = [
    ('elliot', 91),
    ('neelam', 98),
    ('bianca', 81),
    ('elliot', 88),
]
from collections import defaultdict
student_grades = defaultdict(list)
for name, grade in grades:
    student_grades[name].append(grade)
print(dict(student_grades))

import itertools
friends = ['Monique', 'Ashish', 'Devon', 'Bernie']
print(list(itertools.permutations(friends, r=2)))