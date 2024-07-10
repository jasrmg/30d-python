#DAY 11: Functions
#EXERCISES LEVEL 1:
#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
  return a + b
print(add_two_numbers(10, 20))
#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
import math
pi = math.pi
def area_of_circle(r):
  area = pi * r * r
  return f'{area:.2f}'
print(area_of_circle(4))
#3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
  # print(type(nums))
  for value in nums:
    if not isinstance(value, (int, float)):
      return 'There is a non-numeric value in the nums you provided'
  return sum(nums)
print(add_all_nums(1, 2, 3, 4, 5))
print(add_all_nums(1, 2, 3, 4, 5, 'k'))
#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(c):
  fahrenheit = (c * 9/5) + 32
  return fahrenheit
print(convert_celsius_to_fahrenheit(36))
#5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
  autumn = ['September', 'October', 'November']
  winter = ['December', 'January', 'February']
  spring = ['March', 'April', 'May']
  summer = ['June', 'July', 'August']
  season = None
  if month in autumn:
    return 'Autumn'
  elif month in winter:
    return 'Winter'
  elif month in spring:
    return 'Spring'
  elif month in summer:
    return 'Summer'
  else:
    return 'Invalid month!'
print(check_season('February'))
#6. Write a function called calculate_slope which return the slope of a linear 
#skip way formula haha
#7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
#skip wa ko kasabot
#8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(l):
  for elem in l:
    print(elem)
print_list([1, 2, 3, 4, 'a', 'c', 'd'])
#9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(arr):
  rev = []
  for item in range(len(arr)-1, -1, -1):
    rev.append(arr[item])
  return rev
print(reverse_list([1,2,3,4,5]))

# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
#10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(l):
  capitalize = []
  for item in range(0, len(l)):
    capitalize.append(l[item].capitalize())
  return capitalize
print(capitalize_list_items(['a', 'b', 'c']))
#11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst, item):
  new_list = lst
  # for new in item:
  #   new_list.append(new)
  new_list.append(item)
  return new_list
# print(add_item([1, 2, 3], [4, 0]))
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))    #  [2, 3, 7, 9, 5]
#12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item):
  new_list = lst
  if item in lst:
    new_list.remove(item)
  return new_list
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
#13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_all_numbers(number):
  total = 0
  for num in range(1, number + 1):
    total += num
  return total
print(sum_all_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
#14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range
def sum_of_odds(number):
  odd = 0
  for num in range(0, number + 1):
    if num % 2 != 0:
      odd += num
  return odd
print(sum_of_odds(10))
#15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(number):
  even = 0
  for num in range(0, number + 1, 2):
    even += num
  return even
print(sum_of_even(10))
#EXERCISE LEVEL 2:
#1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num):
  even_count = 0
  odd_count = 0
  for n in range(0, num + 1):
    if n % 2 == 0:
      even_count += 1
    else:
      odd_count += 1
  return f"The number of odds are {odd_count}.\nThe number of evens are {even_count}."
print(evens_and_odds(100))
    # print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
#2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
  factorial = 1
  for num in range(1, number + 1):
    factorial *= number
    number -= 1
  return factorial
print(factorial(5))
#3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
  if len(param) == 0:
    return True
  else:
    return False
print(is_empty(food_staff))
#4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# :skip wa ko kasabot

#EXERCISES LEVEL 3:
#1. Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
  divisor = 0
  if number > 1:
    for num in range(1, number + 1):
      if number % num == 0:
        divisor += 1
  if divisor > 2:
    return 'The number is not a prime'
  else:
    return 'The number is prime'
print(is_prime(12))
#2. Write a functions which checks if all items are unique in the list.
def unique(unique_list):
  lst = unique_list
  st = set(unique_list)
  if len(lst) == len(st):
    return 'All the items in the list are unique'
  else:
    return 'The items in the list are not unique'
print(unique([1, 2, 3, 4, 5, 5])) 

#3. Write a function which checks if all the items of the list are of the same data type.
def same_data_type(data_type):
  first_type = type(data_type[0])
  # print(first_type)
  
  for i in data_type[1:]:
    # print(type(i))
    if type(i) != first_type:
      return 'The elements in the list have different data types.'
  return 'The elements in the list has the same data types.'
print(same_data_type([1, 2, 3, 4, 5, 'a', 'b']))
#4. Write a function which check if provided variable is a valid python variable
import keyword
def isvalid(text):
  if not (text[0].isalpha() or text[0] == '_'):
    return False
  
  for char in text[1:]:
    if not (char.isalnum() or char == '_'):
      return False
    
  if keyword.iskeyword(text):
    return False
  
  return True
print(isvalid('for'))
#5. Go to the data folder and access the countries-data.py file.
import countries_data as cd

#6. Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
from collections import Counter
# print(cd.countries_data)
def most_spoken_languages(num):
  languages = []
  for lang in cd.countries_data:
    languages += lang['languages']
  languages_count = Counter(languages)
  top10 = languages_count.most_common(10)
  top20 = languages_count.most_common(20)
  top10_language = ''
  top20_language = ''
  print("type: ", top10[0][0])
  if num == 10:
    print('Top 10 Most Spoken Languages')
    rank = 1
    for lang, count in top10:
      # print('LANG: ',lang)
      # print('COUNT: ',count)
      top10_language += f"{rank}. {lang} - {count}\n"
      rank += 1
    return top10_language
  elif num == 20:
    print('Top 20 Most Spoken Languages')
    rank = 1
    for lang, count in top20:
      top20_language += f"{rank}. {lang} - {count}\n"
      rank += 1
    return top20_language
  else:
    return 'Invalid input! choose between top 10 or top 20 only!'
print(most_spoken_languages(20))
# languages = []
# for lang in cd.countries_data:
#   languages += lang['languages']
# # print(languages)
# languages_count = Counter(languages)
# print(languages_count)
# top_10 = languages_count.most_common(10)
# print(top_10)
# top_20 = languages_count.most_common(20)
# print(top_20)
#7. Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(num):
  # population = []
  # for pop in cd.countries_data:
  #   population.append(pop['population'])
  sorted_population = sorted(cd.countries_data, key=lambda x: x['population'], reverse=True)
  # population = sorted_population
  top_10_population = sorted_population[:10]
  top_20_population = sorted_population[:20]
  top10 = ''
  top20 = ''
  if num == 10:
    print('Top 10 Most Populated Countries:')
    for index, country in enumerate(top_10_population, start=1):
      top10 += f"{index}. {country['name']} - Population: {country['population']}\n"
    return top10
  elif num == 20:
    print('Top 20 Most Populated Countries')
    for index, country in enumerate(top_20_population, start=1):
      top20 += f"{index}. {country['name']} - Population: {country['population']}\n"
    return top20
  else:
    return 'Invalid Input!'
print(most_populated_countries(20))
# population = []
# for pop in cd.countries_data:
#   population.append(pop['population'])
# print(population)