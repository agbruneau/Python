import numpy as np

edges = np.matrix('0 0 0 1; 0 0 1 0; 1 0 0 0; 0 0 1 0')
mat1 = np.matrix('0 0 0 0; 0 0 0 0; 0 0 0 0; 0 0 0 0')

for i in range(0,4):
    for j in range(0,4):
        if edges[i, j] == 1 or (edges[i, 0] == 1 and edges[0, j] == 1):
            mat1[i, j] = 1

print(mat1)
