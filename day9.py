#DAY 9: CONDITIONALS
# #EXERCISE LEVEL 1:
#1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
age = int(input('Enter your age: '))
#or 
# if age > 18:
#   print('You are old enough to drive')
# else:
#   print(f'Wait for ', age - 18, ' years')
print('You are old enough to drive') if age >= 18 else print(f'Wait for ', 18 - age, ' years')

#2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
my_age = 22
your_age = int(input('Enter your age: '))
if your_age > my_age:
  if your_age - my_age > 1:
    print('You are older than me for ', your_age - my_age, ' years!')
  else:
    print('You are older than me for', your_age - my_age, ' year!')
elif my_age > your_age:
  if my_age - your_age > 1:
    print('Im older than you for ', my_age - your_age, ' years!')
  else:
    print('Im older than you for ', my_age - your_age, ' year!')
else:
  print('We have the same age!')
#3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
a = int(input('Enter integer A: '))
b = int(input('Enter integer B: '))
if a > b:
  print(f'{a} is greater than {b}')
elif b > a:
  print(f'{b} is greater than {a}')
else:
  print(f'{a} and {b} are the same!')


#EXERCISE LEVEL 2:
#1. Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
score = int(input('Enter your score: '))
if score >= 80 and score <= 100:
  print('Your grade is: A')
elif score >= 70 and score <= 89:
  print('Your grade is: B')
elif score >= 60 and score <= 69:
  print('Your grade is: C')
elif score >= 50 and score <= 59:
  print('Your grade is: D')
elif score >= 0 and score <= 49:
  print('Your grade is: F')
else:
  print('Invalid score!')
#2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input('Enter a month to check the season: ')
Autumn = ['September', 'October', 'November']
Winter = ['December', 'January', 'February']
Spring = ['March', 'April', 'May']
Summer = ['June', 'July', 'August']
if month in Autumn:
  print('Autumn')
elif month in Winter:
  print('Winter')
elif month in Spring:
  print('Spring')
elif month in Summer:
  print('Summer')
else:
  print('Invalid Month!')
#3. The following list contains some fruits:
#fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ')
if fruit in fruits:
  print('That fruit already exist in the list')
  print(fruits)
else:
  fruits.append(fruit)
  print('That fruit is new, it is added in the list!')
  print(fruits)


#EXERCISE LEVEL 3:
#4. Here we have a person dictionary. Feel free to modify it!
person = {
  'first_name' : 'Jeff Alain',
  'last_name' : 'Sarmago',
  'age' : 22,
  'country' : 'Philippines',
  'is_married' : False,
  'skills' : ['JavaScript', 'Java', 'Python', 'HTML', 'CSS', 'React', 'MongoDB', 'Node'],
  'address' : {
    'street' : 'P.Gomez St.',
    'zipCode' : 6021
  }
}
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
keys = person.keys()
if 'skills' in keys:
  skills = person['skills']
  # print(skills)
  mid = len(skills) // 2
  print(mid)
  if mid % 2 == 0:
    print(skills[mid])
  else:
    print(skills[mid])
    print(skills[mid + 1])
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in keys:
  print('Python is in the skills') if 'Python' in skills else print('Python not found in skills')
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
frontend = ['JavaScript', 'React']
backend = ['Node', 'Python', 'MongoDB']
fullstack = ['React', 'Node', 'MongoDB']
if all(elem in skills for elem in frontend):
  if all(elem in skills for elem in backend):
    print('FULLSTACK!')
  else:
    print('FRONTEND!')
elif all(elem in skills for elem in backend):
  print('BACKEND!')
else:
  print('unknown title, keep grinding!')
#  * If the person is married and if he lives in Finland, print the information in the following format:
#    Asabeneh Yetayeh lives in Finland. He is married.
if person['country'] == 'Philippines' and person['is_married']:
  # print(person['address']['street'])
  print(f"{person['last_name']}, {person['first_name']} lives in {person['address']['street']}.\nZip Code: {person['address']['zipCode']} He is married")
else:
  print(f"{person['last_name']}, {person['first_name']} lives in {person['address']['street']}\nZip Code: {person['address']['zipCode']}. He is not married")