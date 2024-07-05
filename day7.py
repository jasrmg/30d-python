#EXERCISE LEVEL 1:
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1. Find the length of the set it_companies
print(len(it_companies))
#2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
#3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['idk', 'asd', 'test'])
#4. Remove one of the companies from the set it_companies
it_companies.remove('asd')
#5. What is the difference between remove and discard
# remove = shows an error if there is no item in the set, while discard does not throw an error

#EXERCISE LEVEL 2:
#1. Join A and B
A.union(B) 
#2. Find A intersection B
A.intersection(B)
#3. Is A subset of B
A.issubset(B)
#4. Are A and B disjoint sets
A.isdisjoint(B)
#5. Join A with B and B with A
A.union(B)
B.union(A)
#6. What is the symmetric difference between A and B
A.symmetric_difference(B)
#7. Delete the sets completely
del A
del B

#EXERCISE LEVEL 3:
#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print('list: ', len(age))
age = set(age)
print('set: ', len(age))

#2. Explain the difference between the following data types: string, list, tuple and set
#string - is immutable sequence of characters
#list = mutable sequence of elements, ordered.
#tuple = immutable sequence of elements, ordered.
#set = mutable collection of unique elements, unordered.
#3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
words = "I am a teacher and I love to inspire and teach people"
set_words = words.split(' ')
print(type(set_words)) #list
set_words = set(set_words)
print(set_words)
print(type(set_words)) #set