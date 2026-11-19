

import numpy as np

arr = np.arange(1, 11)
print("Experiment 10 - Array from 1 to 10:")
print(arr)


# 2. CREATING ARRAYS

# Create an array from a Python list
a = np.array([1, 2, 3, 4, 5])
print("\nArray using np.array():", a)

# Array filled with zeros
zeros = np.zeros(5)
print("Zeros:", zeros)

# Array filled with ones
ones = np.ones(4)
print("Ones:", ones)

# Empty array (values are uninitialized until assigned)
empty = np.empty(3)
empty[:] = [10, 20, 30]
print("Empty array after assigning values:", empty)

# Range with default step 1
range_array = np.arange(4)
print("np.arange(4):", range_array)

# Range with a step of 2
step_array = np.arange(0, 11, 2)
print("np.arange(0, 11, 2):", step_array)

# Five equally spaced values from 0 to 10
linear_array = np.linspace(0, 10, num=5)
print("np.linspace(0, 10, num=5):", linear_array)

# Specify the data type
integer_ones = np.ones(2, dtype=np.int64)
print("Integer ones:", integer_ones)


matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D array:")
print(matrix)
print("Dimensions:", matrix.ndim)
print("Shape:", matrix.shape)
print("Total elements:", matrix.size)
print("Data type:", matrix.dtype)


values = np.array([10, 20, 30, 40, 50])
print("\nIndexing array:", values)
print("First element:", values[0])
print("Third element:", values[2])
print("Last element:", values[-1])
print("Second-last element:", values[-2])

# Indexing a 2D array: [row, column]
two_d = np.array([[10, 20, 30], [40, 50, 60]])
print("First row, first column:", two_d[0, 0])
print("Second row, third column:", two_d[1, 2])

s = np.array([10, 20, 30, 40, 50, 60])
print("\nSlicing array:", s)
print("Elements at indices 1 to 3:", s[1:4])
print("First three elements:", s[:3])
print("From index 2 to the end:", s[2:])
print("Every second element:", s[::2])
print("Reversed array:", s[::-1])

# Slice rows 0-1 and columns 1-2 from a 2D array
slice_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D slice:")
print(slice_matrix[0:2, 1:3])

unsorted = np.array([2, 1, 5, 3, 7, 4])
print("\nOriginal array:", unsorted)
print("Sorted ascending:", np.sort(unsorted))
print("Sorted descending:", np.sort(unsorted)[::-1])

first = np.array([1, 2, 3])
second = np.array([4, 5, 6])
joined = np.concatenate((first, second))
print("Concatenated arrays:", joined)


x = np.array([10, 20, 30])
y = np.array([2, 4, 5])

print("\nArray x:", x)
print("Array y:", y)
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Element-wise multiplication:", x * y)
print("Division:", x / y)
print("Square of x:", x ** 2)

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

print("\nElement-wise product A * B:")
print(A * B)
print("Matrix product A @ B:")
print(A @ B)
print("Matrix product using dot():")
print(A.dot(B))


data = np.array([1.0, 2.0, 3.0])
print("\nBroadcasting - multiply by 2:", data * 2)
print("Broadcasting - add 5:", data + 5)

row = np.array([10, 20, 30])
column = np.array([[1], [2], [3]])
print("Broadcasting between compatible arrays:")
print(column + row)

numbers = np.array([10, 20, 30, 40, 50])
print("\nNumbers:", numbers)
print("Sum:", np.sum(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
print("Mean:", np.mean(numbers))
print("Product:", np.prod(numbers))
print("Standard deviation:", np.std(numbers))

marks = np.array([70, 80, 90, 85, 75])
print("\nStudent marks:", marks)
print("Total marks:", np.sum(marks))
print("Average marks:", np.mean(marks))
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))

