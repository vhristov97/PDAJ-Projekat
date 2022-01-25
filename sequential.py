import math
import tracemalloc
import time

def parse_point(point):
    coordinate_array = point.split(',')
    x = int(coordinate_array[0])
    y = int(coordinate_array[1])

    return x, y

def calculate_distance(i, j, x, y):
    return math.sqrt((x - i)**2 + (y - j)**2)

def find_min_distance(n, m, points):
    result = []

    for i in range(n):
        for j in range(m):
            min_distance = n + m - 2
            min_index = -1

            for index in range(len(points)):
                x, y = parse_point(points[index])
                distance = calculate_distance(i, j, x, y)

                if(distance < min_distance):
                    min_distance = distance
                    min_index = index
            
            result.append(min_index)

    return result
    

if __name__ == "__main__":
    tracemalloc.start()
    start_time = time.process_time()

    result = find_min_distance(500, 500, ["41,127", "255,241", "411,163", "238,59", "63,127"])
    
    print("METHOD: sequential")

    end_time = time.process_time()
    print(f"Total runtime was {round(end_time - start_time, 5)}s")

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB. Peak was {peak / 10**6}")
    tracemalloc.stop()
    #print(result)