#operators
#day3:
# 1. age = 22
# 2. height = 169.69
# 3. complex_number = 3 + 3j
#area = .5 x b x h
# 4. base = float(input('Enter base: '))
# height = float(input('Enter height: '))
# area = base * height * .5
# print(area)
#5.
# a = int(input('Enter side a: '))
# b = int(input('Enter side b: '))
# c = int(input('Enter side c: '))
# print('The perimeter of the triangle is ', a + b + c)
#6.
length = float(input('Enter length: '))
width = float(input('Enter width: '))
print(format((length + width) * 2, '.2f'))
#7.
pi = 3.14
r = float(input('Enter radius: '))
print(format(2 * pi * r, '.2f'))
#12.
print('LEN: python and dragon: ', len('python') != len('dragon'))
#13
print('on is on python and dragon: ', 'on' in 'python' and 'on' in 'dragon')
#14.
sentence = 'I hope this course is not full of jargon.'
print('jargon' in sentence)
#15.
print('There is no "on" in both dragon and python: ', 'on' not in 'python' or 'on' not in 'dragon')
#16.
text = 'python'
text_length = len(text)
str_text = str(len(text))
float_text = float(len(text))
print(text_length)
print(float_text)
print(str_text)
#17.
print(10 % 2 == 0)
#19.
print('10 is equal to "10"', 10 == '10')
#20
print('9.8 = 10', int(float('9.8')) == 10)
#21
hours = int(input('Enter hours: '))
rph = float(input('Enter rate per hour: '))
print('Your weekly earning is ', int(hours * rph))
#22
years = int(input('Enter number of years you have lived: '))
print('You have lived for ', (years * 31536000), " seconds.")
#23
print("1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")