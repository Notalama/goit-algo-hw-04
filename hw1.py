import random
import timeit
from tabulate import tabulate

def insertion_sort(arr_):
    """Insertion sort an array in place and return it"""
    arr = arr_[:]  # Create a copy to avoid modifying the original array
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr_):
    """Merge sort an array and return a new sorted array"""
    arr = arr_[:]
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    """Merge two sorted arrays into a single sorted array"""
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result


def quick_sort(arr_):
    """Quicksort an array and return a new sorted array"""
    arr = arr_[:]
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def bubble_sort(arr_):
    """Bubble sort an array in place and return it"""
    arr = arr_[:]
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


fn_map = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quicksort": quick_sort,
    "Bubble Sort": bubble_sort,
    "Timsorted": sorted,
    "Timsort": lambda x: x[:].sort(),
}


def get_dataset(size):
    return [random.randint(0, 1000) for _ in range(size)]


def run_tests():
    table = []
    dataset = [get_dataset(100), get_dataset(1000), get_dataset(10000)]

    for name, fn in fn_map.items():
        row = [name]
        for data in dataset:
            row.append(timeit.timeit(lambda: fn(data), number=30))
        table.append(row)
    return table


headers = ["Algorithm", "Small", "Medium", "Large"]


if __name__ == "__main__":
    data = run_tests()
    print(tabulate(data, headers, tablefmt="pipe"))
