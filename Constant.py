import math
import matplotlib.pyplot as plt
min_edge = 3
# Near_r = 8

# def Near_r(n):
#     gamma = 40000
#     kesai_d = math.pi
#     lamda = 8
#     const_1 = math.sqrt((gamma/kesai_d) * (math.log(n)/n))
#     # print('math.log(%i)/%i=%i'%(n,n,math.log(n)/n))
#     # print('const_1=',const_1)
#     const_2 = lamda
#     return min(const_1, const_2)


if __name__=='__main__':
    x = []
    y = []
    for i in range(1000):
        x.append((i+1)*10)
        y.append(Near_r((i+1)*10))
    plt.plot(x,y)
    plt.show()
    # print(Near_r(2000))
    # print(Near_r(1000))
    # print(math.log(2000)/2000)
    # print(math.log(1000)/1000)
    