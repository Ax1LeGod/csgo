# 两数之和
# def sum(a,b):
#     print(a+b)
#
#
# if __name__ == '__main__':
#     sum(1,3)
# 阶乘
# def x(a):
#     b = 1
#     for i in range(1,a+1):
#         b *= i
#         i +=i
#     return b
# if __name__ == '__main__':
#     c=x(6)
#     print(c)

# 圆面积
# import math
# def ymj(a):
#     return math.pi*(a**2)
#
# if __name__ == '__main__':
#     print(ymj(2))

def sushu(a,b):
    list = []
    if a >b or a == 1:
        False
    else:
        for i in range(a, b+1):
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                list.append(i)
    print(list)

if __name__ == '__main__':
    sushu(3,100)





