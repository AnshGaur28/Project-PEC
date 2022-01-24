s1 = int(input('side1: '))
s2 = int(input('side2: '))
s3 = int(input('side 3: '))
sides = [s1,s2,s3]
sides.sort()
print(sides )
if sides[2] <= sides[0] + sides[1] :
    print('Triangle is possible')
else:
    print('Triangle not possible')