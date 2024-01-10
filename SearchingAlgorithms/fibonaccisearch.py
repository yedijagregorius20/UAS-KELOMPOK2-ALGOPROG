import timeit

def fibonacci_search(arr, x):
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib = fib_m_minus_1 + fib_m_minus_2

    while fib < len(arr):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib
        fib = fib_m_minus_1 + fib_m_minus_2

    offset = -1

    def search():
        nonlocal fib, offset, fib_m_minus_1, fib_m_minus_2
        start_time = timeit.default_timer()

        while fib > 1:
            i = min(offset + fib_m_minus_2, len(arr) - 1)

            if arr[i] < x:
                fib = fib_m_minus_1
                fib_m_minus_1 = fib_m_minus_2
                fib_m_minus_2 = fib - fib_m_minus_1
                offset = i

            elif arr[i] > x:
                fib = fib_m_minus_2
                fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
                fib_m_minus_2 = fib - fib_m_minus_1

            else:
                end_time = timeit.default_timer()
                execution_time = end_time - start_time
                return i, execution_time

        if fib_m_minus_1 and arr[offset + 1] == x:
            end_time = timeit.default_timer()
            execution_time = end_time - start_time
            return offset + 1, execution_time

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        return -1, execution_time

    return search()

arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
x = 85

result, execution_time = fibonacci_search(arr, x)

if result != -1:
    print(f"Element found at index {result} with execution time {execution_time:.7f} seconds")
else:
    print("Element not found in the array")