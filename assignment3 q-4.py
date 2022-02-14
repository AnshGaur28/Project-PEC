#grading
gradepoint = int(input('enter your grade between 4 and 10: '))
if gradepoint == 4:
    print('performance= poor & grade letter= D')
elif gradepoint == 5:
    print('Performance=Below average & grade letter = C')
elif gradepoint == 6:
    print('Performance=Average & grade letter = C+')
elif gradepoint == 7:
    print('Performance=good & grade letter = B')
elif gradepoint == 8:
    print('performance=Very good & grade letter = B+')
elif gradepoint == 9:
    print('performance = excellent & grade letter = A')
elif  gradepoint == 10:
    print('Performance = Outstanding & grade letter = A+')
else:
    print('ERROR')

print('END!')
