# Name - Gurdip Singh           SID - 22107007

# Q1
def reverse_string(string):
    return string[::-1]

str = input("Enter a string to reverse : ")
rev_str = reverse_string(str)
print(f"Reversed string is : {rev_str}")



# Q2
n1 = int(input("Enter starting number : "))
n2 = int(input("Enter ending number : "))
n = int(input("Enter divisor number : "))
for i in range(n1, n2+1):
    if i%n==0:
        print(i)



# Q3
def calculate_triangle_area(a, b, c):
    # Check if the combination of sides is possible
    if a + b > c and b + c > a and c + a > b:
        s = (a + b + c) / 2     # Calculate the semi-perimeter

        # Calculate the area using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c))**0.5
        return area
    else:
        return "Invalid combination of sides"

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

area = calculate_triangle_area(a, b, c)
print("Area of the triangle:", area)



# Q4
rows = 5
for i in range(1, rows * 2):
    if i <= rows:
        print("* " * i)
    else:
        print("* " * (2 * rows - i))



# Q5
def print_alphabet_triangle(rows):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0
    for i in range(1, rows + 1):
        for j in range(i):
            print(alphabet[count % 26], end='')
            count += 1
        print()

rows = int(input("Enter the number of rows: "))
print_alphabet_triangle(rows)



# Q6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Prime numbers in the range", start, "to", end, "are:")
for number in range(start, end + 1):
    if is_prime(number):
        print(number)



# Q7
for num in range(1, 501):
    if num % 77 == 0:
        print(num)



# Q8
numbers = []
for _ in range(10):
    num = int(input("Enter an integer: "))
    numbers.append(num)

positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
even_numbers = [num for num in numbers if num % 2 == 0]

occurrences = {}
for num in numbers:
    occurrences[num] = occurrences.get(num, 0) + 1

print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)
print("Number of occurrences:")
for num, count in occurrences.items():
    print(num, "occurs", count, "time(s)")



# Q9
word_list = input("Enter a list of words (separated by spaces): ").split()

word_count = {}
for word in word_list:
    word_count[word] = word_count.get(word, 0) + 1

print("Word count:")
for word, count in word_count.items():
    print(word, "occurs", count, "time(s)")
