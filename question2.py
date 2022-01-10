#QUESTION 2
# All amounts in dollars
standard_deduction = 10000
dependent_deduction = 3000
# deduction per head
gross_income = int(input('what is your gross income ? '))
depends = int(input('how many dependents do you have ? '))

taxable_income = gross_income-(10000+dependent_deduction*depends)
print(taxable_income)
tax = taxable_income*20/100
print(tax)
