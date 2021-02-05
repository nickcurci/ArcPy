#!/usr/bin/env python
# coding: utf-8

# 1. List values
# Using this list:
# [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
# Make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python. 

# In[1]:


a = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
b = []
for number in a:
    if number < 5:
        b.append(number)
print(b)


# In[ ]:





# 2. List overlap
# Using these lists:
# 
# list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
# list_b = ['dog', 'hamster', 'snake']
# Determine which items are present in both lists.
# Determine which items do not overlap in the lists.

# In[2]:


list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']

a = set(list_a)
intersection = a.intersection(list_b)

c = list(intersection)

print(c)


# In[3]:


d = set(list_a).symmetric_difference(list_b)
print(d)


# In[4]:


e = set(list_a) ^ set(list_b)
print(e)


# In[ ]:





# 3. Given a singe phrase, count the occurrence of each word
# Using this string:
# 
# string = 'hi dee hi how are you mr dee'
# Count the occurrence of each word, and print the word plus the count.

# In[5]:


sentence = 'hi dee hi how are you mr dee'

words = sentence.split(' ')
result = {}    
for word in words:                                                                                                                                                                                               
    result[word] = result.get(word, 0) + 1 

total = len(sentence.split())
print('word count:', result)
print('total words:',total)


# 4. User input
# Ask the user for an input of their current age, and tell them how many years until they reach retirement (65 years old).
# 
# Hint:
# 
# age = input("What is your age? ")
# print "Your age is " + str(age)

# In[9]:


age = int(input("What is your age? "))
ret = 65
if age > ret:
    print("stop working, youre too old")
elif age == ret:
    print("you retire this year")
else:
        retage = ret-int(age)
        print("you have ", retage, " years until retirement, yikes...")


# 5. User input 2
# Using the following dictionary, ask the user for a word, and compute the Scrabble word score for that word (Scrabble is a word game, where players make words from letters, each letter is worth a point value):
# 
# letter_scores = {
#     "aeioulnrst": 1,
#     "dg": 2,
#     "bcmp": 3,
#     "fhvwy": 4,
#     "k": 5,
#     "jx": 8,
#     "qz": 10
# }

# In[10]:


letter_scores = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
'y': 4, 'z': 10,}

word = input('Enter a word:')
print('your entered word is:', word)

word_score = 0
for letter in word:
    word_score += letter_scores[letter]

print('your word score is: ', word_score)


# In[ ]:





# In[ ]:




