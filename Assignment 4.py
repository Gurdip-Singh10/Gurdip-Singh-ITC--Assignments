# Name - Gurdip Singh       SID - 22107007

# Ques 1
marks = int(input("Enter the marks: "))

if marks < 25:
    print("Grade: F")
elif marks >= 25 and marks < 45:
    print("Grade: E")
elif marks >= 45 and marks < 50:
    print("Grade: D")
elif marks >= 50 and marks < 60:
    print("Grade: C")
elif marks >= 60 and marks < 80:
    print("Grade: B")
else:
    print("Grade: A")



# Ques 2
year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")



# Ques 3
import random

score = 0

for i in range(10):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 * num2

    print("Question", i+1, ":", num1, "x", num2, "=")
    user_answer = int(input())

    if user_answer == answer:
        print("Right!")
        score += 1
    else:
        print("Wrong. The answer is", answer, ".")

print("You scored", score, "out of 10.")




# Ques 4
n = 0

while True:
    n += 1

    if n % 5 == 2 and n % 6 == 3 and n % 7 == 2:
        print("The jar contains", n, "pieces of candy.")
        break

    if n == 200:
        print("There are less than 200 pieces of candy in the jar.")
        break
