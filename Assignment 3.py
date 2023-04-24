# Ques 1
str = "Python is a case sensitive language"
print(len(str))         # Length of the input string


reversed_string = str[::-1]
# Slice the array from the 1st element to the last element in reverse order.
print(reversed_string)


# print(str.index('a'))
new_str = str[10:len(str)]
print(new_str)


oop_Str = str[0:12] + "object oriented"
print(oop_Str)


print(str.index('a'))

no_space_str = str.replace(" ","")
print(no_space_str)



# Ques 2
name = "ABC"
id = "2110XXXX"
department = "XYZ"
cgpa = 8.1

output = "Hey, {} Here!\nMy SID is {}\nI am from {} department and my CGPA is {}"

print(output.format(name, id, department, cgpa))



# Ques 3
a = 56
b = 10

print(a & b)
print(a | b)
print(a ^ b)
print(a << 2)
print(b << 2)
print(a >> 2)
print(b >> 2)



# Ques 4
num1 = int(input("Enter a no : "))
num2 = int(input("Enter a no : "))
num3 = int(input("Enter a no : "))

if num1>num2:
    if num1 > num3:
        print("num1 is greatest")
    else:
        print("num3 is greatest")

else:
    if num2>num3:
        print("num2 is greatest")
    else:
        print("num3 is greatest")



# Ques 5
input_str = input("Enter a string: ")

if "name" in input_str:
    print("Yes")
else:
    print("No")



# Ques 6
side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))

# Check if the given input lengths can form a triangle
if (side1 > side2 + side3) or (side2 > side1 + side3) or (side3 > side1 + side2):
    print("No")
else:
    print("Yes")