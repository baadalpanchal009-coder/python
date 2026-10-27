
# Session 2 - Counting Characters & Words
# Frequency Dictionary, Word Count Program
# ------------------------------------------------------------------------------------


# Task 1: Count the Frequency of Each Character

"""
text = input("Enter a string: ")

char_frequency = {}

for char in text:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print("Character frequency:", char_frequency)
"""

# ------------------------------------------------------------------------------------


# Task 2: Count Word Frequency in a Food App Review

"""
import string

review = '''
Zomato delivers tasty food.
Zomato offers many food options.
I love the quick delivery.
'''

review = review.lower()

for punctuation in string.punctuation:
    review = review.replace(punctuation, '')

words = review.split()
word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("Word frequency:", word_frequency)
"""

# ------------------------------------------------------------------------------------


# Task 3: Create a Word Frequency Function

"""
def word_freq_dict(text):
    words = text.lower().split()
    word_frequency = {}

    for word in words:
        word = word.strip('.,!?;:')

        if word:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

    return word_frequency


text = 'Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match'

print(word_freq_dict(text))
"""

# ------------------------------------------------------------------------------------


# Task 4: Ignore Common Stopwords

"""
import string

def word_freq_without_stopwords(text):
    stopwords = ['the', 'and', 'in', 'of', 'a', 'to', 'is']

    text = text.lower()

    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')

    words = text.split()
    word_frequency = {}

    for word in words:
        if word not in stopwords:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

    return word_frequency


review = '''
The food is tasty and the delivery is quick.
I like the variety of food in the app.
'''

print(word_freq_without_stopwords(review))
"""

# ------------------------------------------------------------------------------------


# Task 5: Count Characters and Sort the Dictionary

"""
def char_count_dict(text):
    char_frequency = {}

    for char in text:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    return char_frequency


text = input("Enter a string: ")

char_frequency = char_count_dict(text)

sorted_frequency = dict(sorted(char_frequency.items()))

print("Character frequency in sorted order:", sorted_frequency)
"""

# ------------------------------------------------------------------------------------
