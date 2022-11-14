import numpy as np

def solve_det_2(m):
    det_m:float=np.linalg.det(m[:2,:2])
    det_m1:float=-(np.linalg.det(np.delete(m,0,axis=1)))
    det_m2:float=np.linalg.det(np.delete(m,1,axis=1))
    return round(det_m1/det_m,2), round(det_m2/det_m,2)


def main()->None:
    matix=np.array([[1,2,3],[2,5,7]])
    print(solve_det_2(matix))

if __name__ == "__main__":
    main()
