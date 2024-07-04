#LEVEL 1:
#1. Create an empty tuple
my_tpl = tuple() #or my_tpl = ()
#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Jeff', 'Ethan', 'Art', 'Shane', 'Jeño', 'Jayzon', 'Janlie', 'Mark', 'Ghendel')
sisters = ('Julienne',) #need naay comma if isa ra para makuan ni python na tuple siya
#3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
#4. How many siblings do you have?
print(len(siblings))
#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Allen', 'Joy')
family_members = siblings + parents
print(family_members)
#LEVEL 2:
#1. Unpack siblings and parents from family_members
*siblings, parent1, parent2 = family_members 
parents = [parent1, parent2]
print(siblings)
print(parents)
print(parent1)
print(parent2)
#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('potato', 'cluster beans', 'onion', 'turnip')
animal = ('dog', 'chicken', 'pig', 'cow', 'horse')
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)
#3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid_tp = len(food_stuff_tp) / 2
mid_lt = len(food_stuff_lt) / 2
print('tp: ')
if mid_tp % 1 == 0:
  print(food_stuff_tp[int(mid_tp)])
else:
  print(food_stuff_tp[int(mid_tp)])
  print(food_stuff_tp[int(mid_tp) + 1])
print('lt: ')
if mid_lt % 1 == 0:
  print(food_stuff_lt[int(mid_lt)])
else:
  print(food_stuff_lt[int(mid_lt)])
  print(food_stuff_lt[int(mid_lt) + 1])
#5. Slice out the first three items and the last three items from food_staff_lt list
print('first 3: ', food_stuff_lt[:3], '\nlast 3: ', food_stuff_lt[-3:])
#6. Delete the food_staff_tp tuple completely
del food_stuff_tp
#7. Check if an item exists in tuple:
print('pig' in food_stuff_lt)