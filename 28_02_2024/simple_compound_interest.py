# get user input
a = int(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (in percentage): "))
n = int(input("Enter the number of times interest is compounded per year: "))
t = int(input("Enter the number of years: "))

# calculate compound interest
compound_interest = a * (1 + r / 100) ** (n * t) - a

# print the result
print("The compound interest is: ", compound_interest)