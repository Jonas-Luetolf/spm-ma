import numpy as np
def solve_simplex(m):
    #while min(m[-1,:])<0:
    for j in range(3):
        x=np.where(m[-1,:]==min(m[-1,:]))[0][0]
        #---
        n=np.where(m[:-1,-1]/(m[:-1,x]+0.1)==min(i for i in m[:-1,-1]/(m[:-1,x]+0.1) if i>0))[0][0]
        #---
        i=np.where(m[:-1,-1]==m[n,-1])
        i=(i[0][0])
        print(n)
        print(m[n,-1])
        m[i,:]=m[i,:]/m[i,x]
        for y in range(0,m.shape[0]):
            if y==i:
                continue
    
            print(f"{y}:{m[y,i]}")
            m[y,:]=m[y,:]-m[y,i]*m[i,:]
        print("--")

solve_simplex(np.array([[2,1,1,1,0,0,2],[1,2,3,0,1,0,4],[2,2,1,0,0,1,8],[-4,-1,-4,0,0,0,0]],dtype=np.float128))
