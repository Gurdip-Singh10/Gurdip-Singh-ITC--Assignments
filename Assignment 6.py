# Name - Gurdip Singh       SID - 22107007

# Ques 1
def is_perfect_number(number):
    if number <=0:
        return False
    divisors_sum = sum(i for i in range(1,number) if number%i==0)
    if divisors_sum == number:
        print("It is Perfect No")
    else:
        print("It is not a  Perfect No")

a = int(input())
is_perfect_number(a)



# Ques 2
a =input()
b =a[::-1]
if a == b:
    print("Yes")
else:
    print("No")



# Ques 3
def print_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
        triangle.append(row)

    max_width = len(str(triangle[-1][len(triangle[-1]) // 2])) + 1

    for i in range(n):
        row = triangle[i]
        padding = ' ' * ((n - i - 1) * max_width // 2)
        line = ' ' * (max_width // 2)
        for num in row:
            line += str(num).center(max_width)
        print(padding + line)

print_pascals_triangle(5)



# Ques 4
a = input()
b = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','n','p','q','r','s','t','u','v','w','x','y','z',' ']
c = []

for i in a.lower():
    if i not in c:
        c.append(i)

if sorted(b)==sorted(c):
    print('yes')
else:
    print("no")



# Ques 5
str1 = input()
list = str1.split("-")
lis = sorted(list)
str2 = "-".join(lis)
print(str2)



# Ques 6
def student_data(name,student_id,student_class ):
    print(f'student name is {name},SID is {student_id}, class is {student_class}')

name = input()
sid = input()
class_ =input()


student_data(name,sid,class_)



# Ques 7
class Student:
    pass
class Marks:
    pass
student1 = Student()
student2 = Student()
marks1 = Marks()
marks2 = Marks()

print(isinstance(student1, Student))
print(isinstance(student2, Student))
print(isinstance(marks1, Marks))
print(isinstance(marks2, Marks))

print(issubclass(Student, object))
print(issubclass(Marks, object))



# Ques 8
def find_triplets(nums):
    nums.sort()                         # Sort the input list in ascending order
    triplets = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue                    # Skip duplicate elements

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                triplets.append([nums[i], nums[left], nums[right]])

                                        # Skip duplicate elements
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return triplets

nums = [-25, -10, -7, -3, 2, 4, 8, 10]
triplets = find_triplets(nums)
print(triplets)



# Ques 9
class ParenthesesValidator:
    def isValid(self, str):
        mapping = {'(': ')', '[': ']', '{': '}'}
        lis = []
        for idx in str:
            if idx in '([{':
                lis.append(idx)
            elif len(lis) == 0 or idx != mapping[lis.pop()]:
                return False
        return len(lis) == 0
obj = ParenthesesValidator()
print(obj.isValid("([}])"))