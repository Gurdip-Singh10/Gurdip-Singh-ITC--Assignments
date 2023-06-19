# Name - Gurdip Singh       SID - 22107007

# Q4
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Get the input list of marks from the user
n = int(input("Enter the number of students: "))
marks = []

for i in range(n):
    mark = int(input("Enter the mark for student {}: ".format(i + 1)))
    marks.append(mark)

# Sort the list using merge sort
sorted_marks = merge_sort(marks)

# Print the sorted list
print("List after sorting is:", sorted_marks)




# Q5
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


input_array = list(map(int, input("Enter the integer array with duplicates (space-separated): ").split()))

sorted_array = sorted(input_array)
print("Sorted array:", sorted_array)

element = int(input("Enter the element to search: "))

# Perform binary search on the sorted array
index = binary_search(sorted_array, element)

if index == -1:
    print("Element not found.")
else:
    count = 1           # Count the number of occurrences of the element
    left = index - 1
    right = index + 1

    # Count occurrences to the left of the found index
    while left >= 0 and sorted_array[left] == element:
        count += 1
        left -= 1

    # Count occurrences to the right of the found index
    while right < len(sorted_array) and sorted_array[right] == element:
        count += 1
        right += 1

    print("Number of occurrences of element", element, "is:", count)



# Q6
def remove_duplicates(arr):
    return list(set(arr))


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


input_array = list(map(int, input("Enter the integer array (space-separated): ").split()))

unique_array = remove_duplicates(input_array)

print("Sorted array:", sorted(unique_array))

# Sort the array using selection sort
sorted_selection = selection_sort(unique_array)
print("Selection sort:", sorted_selection)

# Sort the array using bubble sort
sorted_bubble = bubble_sort(unique_array)
print("Bubble sort:", sorted_bubble)
