import numpy as np

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
    if num_zeros==0:
        return m
    else:
        for x in range(m.shape[1]-1):
            if m[x,x]==0:
                for y,n in enumerate(m[:,x]):
                    temp_m:np.ndarray=m
                    if n!=0:
                        temp_m[[x,y]]=temp_m[[y,x]]
                        if check_matrix(temp_m)<=num_zeros:
                            m=temp_m
                            num_zeros=check_matrix(m)
                            break
                        else:
                            continue

        if check_matrix(m)!=0:
            print(m)
            raise notsolvable()
        return m


def solve_gauss(m:np.ndarray)->list:
    for x in range(0,m.shape[1]-1):
        m=adjust_matrix(m)
        m[x,:]=m[x,:]/m[x,x]
        
        for y in range(0,m.shape[0]):
            if y==x: continue
            else: m[y,:]=m[y,:]-m[y,x]*m[x,:]
    
    return list(np.around(m,decimals=3)[:,-1])


if __name__ == "__main__":
    matrix:np.ndarray=np.array([[1,0,1],[0,1,2],[1,1,3]],dtype=np.float128)
    
    try:
        results:list=solve_gauss(matrix)
    except notsolvable as exc:
        print(exc)
        exit(-1)

        
    for i,result in enumerate(results):
        print(f"{i+1}. Variable: {result}")
