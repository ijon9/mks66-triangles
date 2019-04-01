import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt(math.pow(vector[0], 2) + math.pow(vector[1], 2) + math.pow(vector[2], 2)) # magnitude is the sqrt(x^2 + y^2 + z^2)
    for i in vector:
        vector[i] = vector[i] / magnitude

#Return the dot product of a . b
def dot_product(a, b):
    return sum([a[0] * b[0], a[1] * b[1], a[2] * b[2]])

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    first = polygons[i]
    second = polygons[i + 1]
    third = polygons[i + 2]
    vector1 = []
    vector2 = []
    for i in range(3):
        vector1.append(second[i] - first[i])
        vector2.append(third[i] - first[i])
    def cross_product(a, b):
        """ Given: a and b are vectors\n
            Returns: vector made from cross product of a and b
        """
        return [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]
    return cross_product(vector1, vector2)
