#DAY 8: DICTIONARIES
#1. Create an empty dictionary called dog
dog = {}
#2. Add name, color, breed, legs, age to the dog dictionary
dog['name'], dog['color'], dog['breed'], dog['legs'], dog['age'] = 'doggy', 'white', 'husky', 4, 2
print(dog)
#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name':'Jeff',
           'last_name':'Sarmago',
           'gender':'Male',
           'age':22,
           'marital_status':'Single',
           'skills':['JS', 'HTML', 'CSS', 'JAVA', 'PYTHON', 'SLEEPING'],
           'country':'Philippines',
           'city':'Argao',
           'address':'Tulic, Argao, Cebu'}
#4. Get the length of the student dictionary
print(len(student))
#5. Get the value of skills and check the data type, it should be a list
print('skills: ', student['skills'])
print(type(student['skills']))
#6. Modify the skills values by adding one or two skills
student['skills'].append('ASDAS')
print('skills: ', student['skills'])
#7. Get the dictionary keys as a list
print(student.keys())
#8. Get the dictionary values as a list
print(student.values())
#9. Change the dictionary to a list of tuples using items() method
print(student.items())
#10. Delete one of the items in the dictionary
student.pop('age')
print(student)
#11. Delete one of the dictionaries
del student