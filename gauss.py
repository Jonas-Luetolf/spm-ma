import numpy as np
import sys

class notsolvable(Exception):
    def __init__(self):
        super().__init__()
    def __str__(self) -> str:
        return "not solvable"

def check_matrix(m:np.ndarray)->int:
    num_zeros:int=0
    for x in range(m.shape[1]-1):
        if m[x,x]==0:
            num_zeros+=1
    return num_zeros

def adjust_matrix(m:np.ndarray)->np.ndarray:
    num_zeros:int=check_matrix(m)
    for x in range(m.shape[1]-1):
        if m[x,x]==0:
            for y,n in enumerate(m[:,x]):
                temp_m:np.ndarray=m
                if n!=0:
                    temp_m[[x,y]]=temp_m[[y,x]]
                    if check_matrix(temp_m)<num_zeros:
                       m[[x,y+x]]=m[[y+x,x]]
                       num_zeros=check_matrix(m)
                       break
                    else:
                        continue
    if check_matrix(m)!=0:
        raise notsolvable()
    return m


def solve_gauss(m:np.ndarray)->list:
    for x in range(0,m.shape[1]-1):
        m[x,:]=m[x,:]/m[x,x]
        
        for y in range(0,m.shape[0]):
            if y==x: continue
            else: m[y,:]=m[y,:]-m[y,x]*m[x,:]
    
    return list(np.around(m,decimals=3)[:,-1])


if __name__ == "__main__":
    matrix:np.ndarray=np.array([[0,1,0,2],[0,0,1,3],[1,0,0,1]],dtype=np.float128)
    if check_matrix(matrix)>0:
        matrix=adjust_matrix(matrix)

        print(matrix)
        results:list=solve_gauss(matrix)

        for i,result in enumerate(results):
            print(f"{i+1}. Variable: {result}")
