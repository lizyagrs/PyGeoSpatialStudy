import numpy as np

def test():
    vector = np.array([1, 2, 3, 4])
    metrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

    result=np.where(metrix < 5, 0, metrix)
    result=np.where(result >= 5, 1, result)
    print(result)
    result2=np.where(metrix >= 5, 1, 0)
    print(result2)

def TwoToOne():
    t1 = np.arange(12)
    print(t1)
    t2 = t1.reshape(3, 4)
    print(t2)

    t3 = t2.reshape(t2.shape[0]*t2.shape[1], )
    print(t3)

    t4 = t2.flatten()
    print(t4)

#主函数
if __name__ == '__main__':
    #获取工程根目录的路径
    TwoToOne()