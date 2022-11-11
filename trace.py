import numpy as np

def trace(A):
    tr=0
    for i in range(np.linalg.matrix_rank(A)):
        tr+=A[i][i]

    return tr

if __name__ == "__main__":
    print(trace(np.array([[1,2],[2,1]])))
