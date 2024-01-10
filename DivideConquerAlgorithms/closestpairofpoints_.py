import timeit
import math

def closest_pair(points):
    def euclidean_distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def brute_force_closest_pair(points):
        min_distance = float('inf')
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = euclidean_distance(points[i], points[j])
                if distance < min_distance:
                    min_distance = distance
        return min_distance

    def closest_pair_recursive(sorted_points):
        n = len(sorted_points)
        if n <= 3:
            return brute_force_closest_pair(sorted_points)

        mid = n // 2
        mid_point = sorted_points[mid]

        left_closest = closest_pair_recursive(sorted_points[:mid])
        right_closest = closest_pair_recursive(sorted_points[mid:])

        min_distance = min(left_closest, right_closest)

        strip = [point for point in sorted_points if abs(point[0] - mid_point[0]) < min_distance]

        strip_closest = min_strip(strip, min_distance)

        return min(min_distance, strip_closest)

    def min_strip(strip, min_distance):
        strip.sort(key=lambda point: point[1])
        strip_length = len(strip)

        for i in range(strip_length):
            j = i + 1
            while j < strip_length and strip[j][1] - strip[i][1] < min_distance:
                min_distance = min(min_distance, euclidean_distance(strip[i], strip[j]))
                j += 1

        return min_distance

    sorted_points = sorted(points, key=lambda point: point[0])

    start_time = timeit.default_timer()
    result = closest_pair_recursive(sorted_points)
    end_time = timeit.default_timer()

    runtime = end_time - start_time
    return result, runtime

points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
closest_distance, runtime = closest_pair(points)

print(f"Closest Pair Distance: {closest_distance}")
print(f"Runtime: {runtime:.6f} seconds")