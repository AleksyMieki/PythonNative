import ctypes
import csv
import numpy as np

lib = ctypes.cdll.LoadLibrary('./newt.dll')


lib.interpolate.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_double, ctypes.c_int]
lib.interpolate.restype = ctypes.c_double

def interpolate(array, x, xi):
    n = len(array)


    array = (ctypes.c_double * n)(*array)
    x = (ctypes.c_double * n)(*x)
    xi = ctypes.c_double(xi)
    n = ctypes.c_int(n)


    result = lib.interpolate(array, x, xi, n)

    return result


with open('dist/data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = list(reader)


nodes = [float(row[0]) for row in data]
points = [float(row[1]) for row in data]


for point in points:
    result = interpolate(nodes, nodes, point)
    print(f'The interpolated value at point {point} is {result}.')

    input()

