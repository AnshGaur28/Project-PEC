month = int(input('give month-'))
if (month in [1,3,5,7,8,10,12]):
    day = int(input('give day-'))
    if(1<=day<=30):
        year = int(input('Give year-'))
        if 1800<=year<=2025:
            print(day,'/',month,'/',year)
            if month==12 and day==31 :
                print(1,'/',1,'/',year+1)
            elif day ==31:
                print('1','/',month+1,'/',year)
            else:
                print(day+1,'/',month,'/',year)
        else:
            print('invalid year')
    else:
        print('invalid date')

elif (month in [ 4,6,9,11]):
    day = int(input('date-'))
    if 1<=day<=30:
        year = int(input('year-'))
        if 1800<=year<=2025:
            print(day,'/',month,'/',year)
            if day==30:
                print(1,month+1,year)
            else:
                print(day+1,month,year)
        else:
            print('invalid year')
    else:
        print('invalid date')
elif month==2:
    year = int(input('year- '))
    if 1800<=year<=2025:
        date = int(input('date- '))
        if year%4==0:
            if 1<=date<=29:
                print(date,'/',month,'/',year)
                if date==29:
                    print(1,'/',month+1,'/',year)
                else:
                    print(date+1,'/',month,'/',year)
            else:
                print('invalid date')
        elif (1<=date<=28):
            print(date,'/',month,'/',year)
            if date==28:
                print(1,'/',month+1,year)
            else:
                print(date+1,'/',month,'/',year)
        else:
            print('invalid date')
    else:
        print('invalid year')
else:
    print('invalid month')
print('complete!')









