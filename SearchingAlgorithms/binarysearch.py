import timeit

def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    def search():
        nonlocal left, right
        start_time = timeit.default_timer()

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == x:
                end_time = timeit.default_timer()
                execution_time = end_time - start_time
                return mid, execution_time

            elif arr[mid] < x:
                left = mid + 1

            else:
                right = mid - 1

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        return -1, execution_time

    return search()

arr = [2,4,6,7,9,11,14,16,19,23,25,28,32,35,39,44,47,50]
x = 7

result, execution_time = binary_search(arr, x)

if result != -1:
    print(f"Element found at index {result} with execution time {execution_time:.7f} seconds")
else:
    print("Element not found in the array")