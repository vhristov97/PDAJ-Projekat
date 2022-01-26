import math
import tracemalloc
import time
from multiprocessing import Pool
from os import cpu_count

PARSED_POINTS = []

def parse_points(points):                                                                   #parsira sve specijalne tacke u listu
    for point in points:                                                        
        PARSED_POINTS.append(parse_point(point))

def parse_point(point):                                                                     #parsira pojedinacne specijalne tacke
    coordinate_array = point.split(',')
    x = int(coordinate_array[0])
    y = int(coordinate_array[1])

    return x, y

def calculate_distance(i, j, x, y):                                                         #racuna rastojanje
    return math.sqrt((x - i)**2 + (y - j)**2)

def find_closest_sp(point):                                                                 #pronalazi index najblize specijalne tacke za koordinate matrice (i, j)
   all_distances = [calculate_distance(point[0], point[1], x, y) for x, y in PARSED_POINTS]
   return all_distances.index(min(all_distances))

def compute(n, m, points):
    matrix = [(i,j) for i in range(n) for j in range(m)]                                    #pakuje matricu u listu
    parse_points(points)

    with Pool() as pool:
        result = pool.map(find_closest_sp, matrix)                                         #formira listu najblizih index-a
    
    return result
    
if __name__ == "__main__":
    tracemalloc.start()
    start_time = time.process_time()
    
    #result = compute(10, 10, ["1,3", "3,2", "6,8", "9,6", "5,5"])
    result = compute(500, 500, ["41,127", "255,241", "411,163", "238,59", "63,127"])
    
    print("METHOD: multiprocessing")

    end_time = time.process_time()
    print(f"Total runtime was {round(end_time - start_time, 5)}s")

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB. Peak was {peak / 10**6}MB")
    tracemalloc.stop
    #print(result)