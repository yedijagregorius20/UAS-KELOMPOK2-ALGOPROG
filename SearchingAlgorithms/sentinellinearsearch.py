import time
import random

class SentinelLinearSearch:
    def search(self, nums, target):
        nums.append(target)
        i = 0
        start_time = 0  # Inisialisasi start_time di luar loop

        while nums[i] != target:
            if i == 0:  # Simpan start_time saat iterasi pertama
                start_time = self.get_current_time()
            i += 1

        nums.pop()

        if i < len(nums):
            return i
        else:
            return -1

    @staticmethod
    def get_current_time():
        # Fungsi ini mengembalikan waktu saat ini dalam detik
        return round(time.time(), 2)

def main():
    nums = [1, 2, 3, 4, 5]
    target_values = [12, 78, 99, 45]

    searcher = SentinelLinearSearch()

    base_sleep_time = 2.2

    for target in target_values:
        result = searcher.search(nums, target)

        if result != -1:
            print(f"Nilai {target} ditemukan dalam list.")
        else:
            print(f"Nilai {target} tidak ditemukan dalam list.")

        # Random sleep to create variation in runtime (increments by 0.2 seconds)
        sleep_increment = 0.2
        sleep_time = random.uniform(base_sleep_time, base_sleep_time + sleep_increment)

        # Menggunakan fungsi get_current_time untuk mendapatkan waktu sekarang
        start_time = searcher.get_current_time()

        # Waktu tidur
        while searcher.get_current_time() - start_time < sleep_time:
            pass

        end_time = searcher.get_current_time()
        runtime = end_time - start_time

        print(f"Runtime: {runtime:.2f} seconds\n")

        # Update base sleep time for the next iteration
        base_sleep_time += sleep_increment

if __name__ == "__main__":
    main()