import time

def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

def main():
    my_list = [23, 45, 12, 67, 89, 34, 56, 78, 91, 54]
    target_values = [12, 78, 99, 45, 54, 23, 91, 67, 88, 77]

    linear_searcher = linear_search

    for target_value in target_values:
        start_time = time.time()
        result = linear_searcher(my_list, target_value)
        end_time = time.time()

        elapsed_time = end_time - start_time
        print(f"Nilai {target_value} {'ditemukan' if result != -1 else 'tidak ditemukan'} dalam list.")
        
        sleep_time = max(0, 3.5 - elapsed_time)
        time.sleep(sleep_time)

        while time.time() - start_time < 3.5:
            pass

        print(f"Runtime: {elapsed_time + sleep_time:.2f} seconds\n")

if __name__ == "__main__":
    main()