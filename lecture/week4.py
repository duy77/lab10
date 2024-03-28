t = ['a', 'b', 'c', 'd', 'e', 'f']
    # 0    1    2    3    4    5
#print(t[0])
#print(t[-2:-1])
# # left part is the first element to be included, index starts at 0
# right part is the first element to be excluded
#print(t[2:4])
#print(t[:])
#print(t)
#print(t[2:3])
#print(t[2])

name = "duy"
course = "python"

person = {'name': name, 'course': course, 'name': 'someone else'}
#for key in person:
 #   print(key)
 #   print(person[key])
    
# # items returns a list of key-value pairs
for key, value in person.items():
     print(key, value)
# # keys, values, items are all list-like objects
#print(person.keys())
# print('name' in person.keys())
# print(person.values())
# print(person.items()) # return a list of key-value pairs

