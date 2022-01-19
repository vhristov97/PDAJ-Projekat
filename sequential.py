import math

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
    result = find_min_distance(10, 10, ["1,3", "3,2", "6,8", "9,6", "5,5"])
    print(result)