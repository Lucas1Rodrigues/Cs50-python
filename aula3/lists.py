# lists tuples and sets

courses = ['art','math','geometry','history']
courses.append('Portuguese')
courses.insert(5,'Geography')
courses.remove('history')

courses2 = ['Lucas','Rodrigues']
courses.extend(courses2)
courses.sort()



print(courses)
print(courses[-1])
print(courses[2])
