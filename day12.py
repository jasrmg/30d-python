#DAY 12: MODULES
# from module_test import test as t, add as a, squared as s, upper as u, capital as c
# print(t('jeff', 'saarm'))
# print('add: ', a(10, 20, 30))
# print('squared: ', s(5))
# print('upper: ', u("upper"))
# print('capital: ', c('capital'))

# from random import random, randint
# print(f"{random():.2f}")
# print(randint(1, 10))

#EXERCISE LEVEL 1:
#1. Writ a function which generates a six digit/character random_user_id.
#  print(random_user_id());
#   # '1ee33d'
import string
import random
from random import randint

def random_user_id():
  pool = string.ascii_lowercase + string.digits 
  random_chars = [random.choice(pool) for _ in range(6)]
  return ''.join(random_chars)

print(random_user_id())
#2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf
# def user_id_gen_by_user():
#   pool = string.ascii_letters + string.digits
#   numchar = int(input('Enter the number of characters: '))
#   numId = int(input('Enter the number of IDs to be made: '))
#   lst = []
#   word = ''
#   for i in range(0, numId):
#     ids = [random.choice(pool) for _ in range(numchar)]
#     word = ''.join(ids)
    
#     lst.append(word)
#   return '\n'.join(lst)
  
# print(user_id_gen_by_user())
   
# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr
#3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
def rgb_color_gen():
  rgb = []
  num = 0
  for i in range (0, 3):
    num = randint(0, 255)
    rgb.append(num)
  return f"rgb{tuple(rgb)}"
print(rgb_color_gen())


#EXERCISE LEVEL 2:
#1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors():
  # color = []
  # for _ in range(1):
  #   hex_code = '#' + ''.join(random.choice('0123456789ABCDEF') for _ in range(6))
  #   color.append(hex_code)
  # return ''.join(color)
  #parehas sa js na ako nabuhat
  hexadecimal = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
  hex = ''
  rnum = 0
  for i in range(0,6):
    rnum = randint(0, 14)
    hex += hexadecimal[rnum]
  return f"#{hex.upper()}"
print(list_of_hexa_colors())
#2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors():
  color = ()
  for _ in range(1):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color += (red, green, blue)
  return f"rgb{color}"
print(list_of_rgb_colors())
#3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(choice, num):
  if choice == 'hexa':
    color = []
    for _ in range(num):
      hex_code = '#' + ''.join(random.choice('0123456789ABCDEF') for _ in range(6))
      color.append(hex_code)
    return f"{num} - HEX : \n{'   '.join(color)}"
  elif choice == 'rgb':
    rgb = ''
    all_rgb = f'{num} - RGB:\n'
    for _ in range(num):
      red = random.randint(0, 255)
      green = randint(0, 255)
      blue = randint(0, 255)
      rgb = f"rgb({red}, {green}, {blue})\n" 
      all_rgb += rgb 
    return all_rgb
  else:
    return 'Invalid choice!' 

print(generate_colors('hexa', 5))
print(generate_colors('rgb', 5))

#EXERCISE LEVEL 3:
#1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
  input_list = lst
  random.shuffle(input_list)
  return input_list

sample = [1, 2, 3, 4, 5]
print(shuffle_list(sample))
#2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def nine_unique_num():
  st = set()
  while len(st) < 7:
    st.add(randint(0, 9))
  return list(st)
print(nine_unique_num())
