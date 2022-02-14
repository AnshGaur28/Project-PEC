#intersection &
#difference -
#symm diff ^
# | union
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}
print(set1^set2) #a
print(set1^set2^set3) #b

new_set = {1,2,3,4,5,6,7,8,9}
print(new_set-set1)#d

print(new_set-set1-set2-set3)#e
print((set1&set2)|(set2&set3)|(set1&set3))#c

