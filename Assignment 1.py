# name = Gurdip Singh      SID - 22107007

# Ques1
# ask user to input three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# calculate the average
average = (num1 + num2 + num3) / 3

# print the result
print("The average is", average)


# Ques 2
# ask user for gross income and number of dependents
gross_income = float(input("Enter your gross income: "))
num_dependents = int(input("Enter the number of dependents: "))

# calculate taxable income
standard_deduction = 10000
dependent_deduction = 3000
taxable_income = gross_income - standard_deduction - (dependent_deduction *
                                                      num_dependents)

# calculate tax
tax_rate = 0.20
tax = taxable_income * tax_rate

# display results to user
print("Your taxable income is: $", taxable_income)
print("Your tax is: $", tax)


# Ques 3
# ask user for number of seconds
seconds = int(input("Enter the number of seconds: "))

# calculate minutes and seconds
minutes = seconds // 60
remaining_seconds = seconds % 60

# display result to user
print(seconds, "seconds is equal to", minutes, "minute(s) and",
      remaining_seconds, "second(s)")


# Ques 4
# define the three numbers as variables
num1 = 25
num2 = '25'
num3 = 25.0

# convert num2 to an integer
num2_int = int(num2)

# add the three numbers together
result = num1 + num2_int + num3

# convert the result to a string
result_str = str(result)

# display the result as a string
print("The result is:", result_str)


# Ques 5
import math

for angle in range(0, 346, 15):
    radians=math.radians(angle)
    sine=round(math.sin(radians),4)
    cosine=round(math.cos(radians),4)
    print(f"{angle}, {sine}, {cosine}")


