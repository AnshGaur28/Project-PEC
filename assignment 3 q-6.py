#a
student = dict()
answer = 'y'
while answer == 'y': # for infinite loop until we end it
    sid = int(input('SID: '))
    name = input('student name: ')
    student[sid] = name
    answer = input('y or n : ')

print(student)# gives us the dictionary

#d
a =  input('name of student: ')
b = int(input('SID: '))
print(student[b])

#B sorting by SID(key)
print(sorted(student.items()))#as a  tuple
print(sorted((student)))#as a list of keys

#c sorting by name(value)
newdict = dict()
for k,v in student.items():
    newdict[v] = k # reversing key value pairs in new dictionary
print(sorted(newdict.items()))







