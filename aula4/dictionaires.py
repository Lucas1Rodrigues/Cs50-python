student = {'name': 'Lucas', 'age': 26, 'courses': ['Math','CompSci']}

print(student.get('name'))
"""student['phone'] = '555-5555'
student['name'] = 'Miguel'
print(student.get('phone', 'Not Found'))"""
student.update({'name': 'Miguel', 'age': 2, 'courses': ['Primary']})
student.pop('age')
student['colour hair'] = 'black'
print(student)
print(student.keys())
print(student.values())
print(student.items())