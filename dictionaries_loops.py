student1 = {'name': 'Hamza', 'gpa': 3.8, 'lastName': 'hamrokulov'}
student2 = {'name': 'Alexa', 'gpa': 3.9, 'lastName': 'mois'}
print("****************************# Looping with keys")
for key in student1:
    print('key is:', key)

for key in sorted(student1.keys()):
    print('key in:', key)

print("****************************# Looping the values")
for value in student1:
    print('value is:', student1[value])

for value in student1.values():
    print('value is:', value)

print("***************************# Lopping key and value")
for dkey, dvalue in student1.items():
    print('key is:', dkey)
    print('value is:', dvalue)
    print()

print('****************************Nesting dictionaries in list')
class_2020 = [student1, student2]
print(class_2020)
for student in class_2020:
    print('name of the student:', student['name'])
    print('GPA of the student:', student['gpa'])
    print('last name of the student:', student['lastName'])
    print()

print('****************************Nesting dictionaries in Dictionaries')

dclass_2020 = {'student1': student1, 'student2': student2}
print(dclass_2020)
print(class_2020)
for key, value in dclass_2020.items():
    print('key of the element:', key)
    print('value of the element:', value)
    print('name of the student:', value['name'])
    print('GPA of the student:', value['gpa'])
    print('last name of the student:', value['lastName'])

    print()





