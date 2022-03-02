class Student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
p1 = Student('Ansh',21103022)
print(p1.name)
print(p1.roll_number)
del p1

# print(p1.name) gives error of no attributes as they were deleted .



