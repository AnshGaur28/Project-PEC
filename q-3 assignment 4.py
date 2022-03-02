v1 = int(input('value 1 : ' ))
v2 = int(input('value 2 : ' ))
q,r = (v1//v2,v1%v2) # yes (function/value) is possible
print(q)
print(r)

#b)
def check(n): # defining function to check if values are zero or non zero
    if v1 == 0:
        print(n,' is zero')
    else:
        print(n,' is non-zero')
check(v1)
check(v2)
check(q)
check(r)
#C
sett = set()
#D
sett = {v1,v2,q,r,4,5,6}
print(sett)
for n in sett : # filter function to filter out some values
    filtered = filter(lambda n:n>=4,sett)
filtered_set = set(filtered)
print(filtered_set)
#E
immutable_set = print(frozenset(filtered_set)) #making a set immutable
#F
print('max value: ',max(filtered_set))
print('HASH value: ',hash(max(filtered_set)))































