import math
import tracemalloc
import time

def generate_matrix(n, m):
    for i in range(n):
        for j in range(m):
            yield i, j

def parse_points(points):                                                   #parsira sve specijalne tacke u listu
    return [parse_point(point) for point in points] 

def parse_point(point):                                                     #parsira pojedinacne specijalne tacke
    coordinate_array = point.split(',')
    x = int(coordinate_array[0])
    y = int(coordinate_array[1])

    return x, y

def calculate_distance(i, j, x, y):                                         #racuna rastojanje
    return math.sqrt((x - i)**2 + (y - j)**2)

def find_closest_sp(i, j, points):                                          #pronalazi index najblize specijalne tacke za koordinate matrice (i, j)
   all_distances = [calculate_distance(i, j, x, y) for x, y in points]
   return all_distances.index(min(all_distances))

def generate_results(matrix, parsed_points):                                #wrapper za formiranje generatora
    for i, j in matrix:
        yield find_closest_sp(i, j, parsed_points) 

def compute(n, m, points):
    matrix = generate_matrix(n, m)                                          #pakuje matricu u listu
    parsed_points = parse_points(points)

    result = generate_results(matrix, parsed_points)
    return result
    
if __name__ == "__main__":
    tracemalloc.start()
    start_time = time.process_time()

    result = compute(500, 500, ["41,127", "255,241", "411,163", "238,59", "63,127"])

    print("METHOD: generators")

    end_time = time.process_time()
    print(f"Total runtime was {round(end_time - start_time, 10)}s")

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB. Peak was {peak / 10**6}")
    tracemalloc.stop()
    #result_list = "[" + str(next(result))
    #for index in result:
    #    result_list += ", " + str(index)
    #result_list += "]"

    #print(result_list)