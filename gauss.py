import numpy as np
import sys

def check_matrix(m:np.ndarray)->bool:
    for x in range(m.shape[1]-1):
        if m[x,x]==0:
            return False
    return True

def adjust_matrix(m):
    for x in range(m.shape[1]-1):
        if m[x,x]==0:
            for y,n in enumerate(m[x:,x]):
                if n!=0:
                    m[[x,y+x]]=m[[y+x,x]]
                    break

    if not check_matrix(m):
        sys.exit(-1)
        
    return m


def solve_gauss(m):
    for x in range(0,m.shape[1]-1):
        m[x,:]=m[x,:]/m[x,x]
        
        for y in range(0,m.shape[0]):
            if y==x: continue
            else: m[y,:]=m[y,:]-m[y,x]*m[x,:]
    
    return list(np.around(m,decimals=3)[:,-1])


if __name__ == "__main__":
    matrix=np.array([[4,6,2,22],[3,0,2,9],[5,1,1,10]],dtype=np.float128)
    if not check_matrix(matrix):
        matrix=adjust_matrix(matrix)


        results=solve_gauss(matrix)

        for i,result in enumerate(results):
            print(f"{i+1}. Variable: {result}")
