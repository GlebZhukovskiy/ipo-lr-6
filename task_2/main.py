import random

num =  [-3, -5, -2, -12, 0, 15, 4, 7, 2]

a = random.randint(4, 8)
b = random.randint(4, 8)

matrix = []

for i in range(a):
    c = []
    for j in range(b):
        c.append(num[(i * b + j) % len(num)])
    matrix.append(c)
print(matrix)

for c in matrix:
    