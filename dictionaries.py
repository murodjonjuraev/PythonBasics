# # Dictionaries - as DATA structure, mutable, {key1: value1, key2: value2}
# # List - Data structure, mutable, [a, b]
# cars = ['lexus', 'bugatti', 'bmw', 'ferrari']
# # Tuples - Data structure, immutable, (a, b)
# cars = ('lexus', 'bugatti', 'bmw', 'ferrari')
#
# # Stores the values as key value pair
# # Must know:
# # create, modify (add element, remove elements, reset). Loop through elements
# students = {}  # this is empty dictionary
# students1 = dict()  # creates empty dictionary, converts to dictionary
#
# student1 = {'name': 'Hamza', 'gpa': 3.8}
# student2 = {'name': 'Alexa', 'gpa': 3.9}
# #  accessing the values of Dictionary, as in list with >> cars = [0]
# print(student1)
# print(student1['name'], student1['gpa'])
# print(f" Next student is {student2['name']} with gpa = {student2['gpa']}")
#
# # Assigning the value
# student1['gpa'] = 3.7  # if ke is existing  this will reset the value
# print(student1)
#
# student1['state'] = 'NY'  # if key not exist, then it will crate new key-value pair
# print(student1)
# print(sorted(student1))
#
# del student1['state']
# print(student1)

#
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
#
# new_points = alien_0['points']
# print(f"You just earned {new_points}  points!")
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {}
# alien_0['coloe'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")
#
# alien_0['color'] = 'yellow'
# print(f"the alien color now is {alien_0['color']}.")
#
# alien_o = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original x_position: {alien_o['x_position']}")
# alien_o['speed'] = 'fast'  # to change speed of alien
# if alien_o['speed'] == 'slow':
#     x_increment = 1
# elif alien_o['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_o['x_position'] = alien_o['x_position'] + x_increment
# print(f"New position: {alien_o['x_position']}")
#
# # del alien_o['speed']
# # print(alien_o)
#
# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
#     }
# print(f"Sarah's favorite language is {favorite_language['sarah'].title()}.")

########################## Home work ##################################################
friend = {'first_name': 'Cristiano', 'last_name': 'Ronaldo', 'age': 36, 'city': 'Turin'}
print(friend['first_name'], friend['last_name'], friend['age'], friend['city'])

names1 = ['rahim', 'dilovar', 'dilshod', 'bobir', 'bakha']
names = {'rahim': 1, 'dilovar': 2, 'dilshod': 3, 'bobir': 4, 'bakha': 5}
print(f"{names1[0]}'s favorite number is {names['rahim']}")
print(f"{names1[1]}'s favorite number is {names['dilovar']}")
print(f"{names1[2]}'s favorite number is {names['dilshod']}")
print(f"{names1[3]}'s favorite number is {names['bobir']}")
print(f"{names1[4]}'s favorite number is {names['bakha']}")




