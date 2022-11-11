import numpy as np
import time



def det(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]
matrix=np.array([[1,2,3],[4,5,6]])


start1=time.time_ns()
for i in range(10**6):
    np.linalg.det(matrix)
end1=time.time_ns()

start2=time.time_ns()
for i in range(10**6):
    det(matrix)
end2=time.time_ns()

print(end1-start1)
print(end2-start2)
