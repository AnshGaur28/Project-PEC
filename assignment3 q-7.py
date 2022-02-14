# Fibonacci sequence
first_term = int(input('term1: '))
secondterm = int(input('term2: '))
series = [first_term,secondterm]
n = "y"
while n=='y' :
    series.append(series[len(series)-1]+series[len(series)-2])
    print(series)
    n = input('y or n : ')
print(series)

sum =0
for i in series:
    sum+=i
print('Average: ',sum/len(series))



