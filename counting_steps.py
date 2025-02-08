import random
import matplotlib.pyplot as plt

# Insertion Sort
def insertion_sort(arr):
    steps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            steps += 1
        arr[j + 1] = key
    return steps

# Merge Sort
def merge_sort(arr):
    steps = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        steps += merge_sort(left_half)
        steps += merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            steps += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            steps += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            steps += 1

    return steps

# Heap Sort
def heapify(arr, n, i):
    steps = 0
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        steps += 1
        steps += heapify(arr, n, largest)
    
    return steps

def heap_sort(arr):
    steps = 0
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        steps += heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        steps += 1
        steps += heapify(arr, i, 0)

    return steps

# Quick Sort
def partition(arr, low, high):
    steps = 0
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            steps += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    steps += 1
    return i + 1, steps

def quick_sort(arr, low, high):
    steps = 0
    if low < high:
        pi, partition_steps = partition(arr, low, high)
        steps += partition_steps
        steps += quick_sort(arr, low, pi - 1)
        steps += quick_sort(arr, pi + 1, high)
    return steps

# Test different input sizes and record the number of steps
input_sizes = list(range(10, 1010, 20))  # Now from 10 to 1000, step of 10
insertion_steps = []
merge_steps = []
heap_steps = []
quick_steps = []

print("Steps for each algorithm with different input sizes:\n")

for n in input_sizes:
    arr = random.sample(range(n), n)

    # Insertion Sort
    arr_copy = arr.copy()
    insertion_step_count = insertion_sort(arr_copy)
    insertion_steps.append(insertion_step_count)
    print(f"Insertion Sort for n={n}: {insertion_step_count} steps")

    # Merge Sort
    arr_copy = arr.copy()
    merge_step_count = merge_sort(arr_copy)
    merge_steps.append(merge_step_count)
    print(f"Merge Sort for n={n}: {merge_step_count} steps")

    # Heap Sort
    arr_copy = arr.copy()
    heap_step_count = heap_sort(arr_copy)
    heap_steps.append(heap_step_count)
    print(f"Heap Sort for n={n}: {heap_step_count} steps")

    # Quick Sort
    arr_copy = arr.copy()
    quick_step_count = quick_sort(arr_copy, 0, len(arr_copy) - 1)
    quick_steps.append(quick_step_count)
    print(f"Quick Sort for n={n}: {quick_step_count} steps")

# Plot the results
plt.figure(figsize=(10, 6))
#plt.plot(input_sizes, insertion_steps, label='Insertion Sort', marker='o')
plt.plot(input_sizes, merge_steps, label='Merge Sort', marker='o')
plt.plot(input_sizes, heap_steps, label='Heap Sort', marker='o')
plt.plot(input_sizes, quick_steps, label='Quick Sort', marker='o')

# Plotting x^2 and x*log(x) for comparison
import numpy as np
x = np.array(input_sizes)
#plt.plot(x, x**2, label='x^2 (Quadratic)', linestyle='--')
plt.plot(x, x * np.log2(x), label='x*log(x)', linestyle='--')

plt.xlabel('Input Size (n)')
plt.ylabel('Number of Steps')
plt.title('Number of Steps vs Input Size')
plt.legend()
plt.grid(True)
plt.show()
