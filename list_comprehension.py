import math

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

def compute(n, m, points):
    matrix = [(i,j) for i in range(n) for j in range(m)]                    #pakuje matricu u listu
    parsed_points = parse_points(points)

    result = [find_closest_sp(i, j, parsed_points) for i, j in matrix]      #formira listu najblizih index-a
    return result
    

if __name__ == "__main__":
    result = compute(10, 10, ["1,3", "3,2", "6,8", "9,6", "5,5"])
    print(result)