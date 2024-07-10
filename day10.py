#DAY 10: LOOPS
#EXERCISE LEVEL 1:
#1. Iterate 0 to 10 using for loop, do the same using while loop.
for num in range(0, 11):
  print(num)

num = 0
while num <= 10:
  print(num)
  num += 1
#2. Iterate 10 to 0 using for loop, do the same using while loop.
for num in range(10, -1, -1):
  print(num)

num = 10
while num >= 0:
  print(num)
  num -= 1
#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
count = '#'
for i in range(0, 8):
  print(count)
  count += '#'
  #or
for i in range(1, 9):
  print('#' * i)
#4. Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for i in range(1, 9):
  for j in range(1, 9):
    print('#', end=' ')
  print()
#5. Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for i in range(0, 11):
  print(f'{i} x {i} = ', i * i, '\n')
#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in lst:
  print(item)
#7. Use for loop to iterate from 0 to 100 and print only even numbers
for num in range(0, 101):
  if num % 2 == 0:
    print(num)
#8. Use for loop to iterate from 0 to 100 and print only odd numbers
for num in range(0, 101):
  if num % 2 != 0:
    print(num)
#EXERCISE LEVEL 2:
#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total = 0
for num in range(0, 101):
  total += num
print('The sum of all numbers is ', total, '.')
#2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even_sum = 0
odd_sum = 0
for num in range(0, 101):
  if(num % 2 == 0):
    even_sum += num
  else:
    odd_sum += num
print('The sum of all evens is ', even_sum, '. And the sum of all odds is ', odd_sum, '.')

#EXERCISE LEVEL 3:
#1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from countries import countries
for country in countries:
  if 'land' in country:
    print(country) 
#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit = ['banana', 'orange', 'mango', 'lemon']
reverse_fruit = []
for item in range(len(fruit) -1, -1, -1):
  reverse_fruit.append(fruit[item])
print(reverse_fruit)
#3. Go to the data folder and use the countries_data.py file.
from countries_data import countries_data
#3.1 What are the total number of languages in the data
languages = []
for country in countries_data:
  languages += country['languages']
# languages.append('Bisaya')
print('languages: ', languages)
languages_count = len(languages)
print('Total language count: ', languages_count)
#3.2 Find the ten most spoken languages from the data
from collections import Counter
languages_count = Counter(languages) #iphon kapila ga balik2 ang language
top_ten_languages = languages_count.most_common(10)
rank = 1
for language, count in top_ten_languages:
  print(f'{rank}. {language}: {count}')
  rank += 1

for country in countries_data:
  print(country)
#3.3 Find the 10 most populated countries in the world
#di magamit ang Count diri kay ang Count para ra sa strings(?)

sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
#by default ang sorted kay i sort siya in ascending order(1,2,3,4,5) so ang pinakagamay moy mauna if asc. maong g reverse true kay para ma desc(5,4,3,2,1)
#lambda: takes x as an argument nga ni represent sa elements sa dictionary ang iya i return kay x['population]
#function siya pero maba ug pwede 1 line. pero d siya ma reuse
#pwede bsan pila nga parameter pero isa ra ka expression ang mabuhat
top_ten_languages = sorted_countries[:10]
# print("TOP 10: ",top_ten_languages)
print('Top 10 populated countries:')
for index, country in enumerate(top_ten_languages, start=1):
  print(f"{index}. {country['name']} - Population: {country['population']}")