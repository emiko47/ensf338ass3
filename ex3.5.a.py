import random
import timeit
import matplotlib.pyplot as plt

# Ineffiient Implementation
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Efficient Implementation
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


# Generate a sorted array of random integers
arr = sorted(random.sample(range(10000), 1000))

# Measure the execution time of linear search and binary search for 100 trials
linear_times = []
binary_times = []
for i in range(100):
    target = random.randint(0, 9999)
    linear_time = timeit.timeit(lambda: linear_search(arr, target), number=1000)
    binary_time = timeit.timeit(lambda: binary_search(arr, target), number=1000)
    linear_times.append(linear_time)
    binary_times.append(binary_time)

# Plot the distribution of measured values
plt.hist(linear_times, bins=20, alpha=0.5, label='linear')
plt.hist(binary_times, bins=20, alpha=0.5, label='binary')
plt.legend(loc='upper right')
plt.show()

# Print the aggregate of measured values
print('Linear Search: min =', min(linear_times), 'avg =', sum(linear_times) / len(linear_times))
print('Binary Search: min =', min(binary_times), 'avg =', sum(binary_times) / len(binary_times))
