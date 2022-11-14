import numpy as np

def solve_gauss(m):
    for x in range(0,m.shape[1]-1):
        m[x,:]=m[x,:]/m[x,x]
        
        for y in range(0,m.shape[0]):
            if y==x: continue
            else: m[y,:]=m[y,:]-m[y,x]*m[x,:]
    
    return list(np.around(m,decimals=3)[:,-1])


if __name__ == "__main__":
    matrix=np.array([[4,9,-8,5],[3,-6,16,5],[5,3,4,7]],dtype=np.float128)
    results=solve_gauss(matrix)

    for i,result in enumerate(results):
        print(f"{i+1}. Variable: {result}")
