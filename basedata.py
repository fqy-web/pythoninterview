# 问题描述：给定一个整数x，计算它的二进制形式中包含多少个1
# 暴力枚举法
'''
import time
x = bin(int(input('>>')))
a = time.time()

count = 0
print(x)
for i in x:
    if i == '1':
        count += 1

print('count:', count)
a = time.time() - a
print(a,'s')
'''
# 更优解
# 实现思路为二进制形式中有几个1就执行几次循环，复杂度为1的个数，而不用遍历每个数
# x&=(x-1)的作用是将x二进制形式中最右边的1抹除掉，即转换为0
'''
def countOnes(x):
    count = 0
    while x > 0:
        count += 1
        x&= (x-1)
    return count

import time
a = time.time()
c = countOnes(1234)
print('binary form of 1234 is {}'.format(bin(1234)))
print('binary form of 1234 contains {} ls'.format(c))
a = time.time() - a    # 计算函数执行所需的时间
print(a, 's')
'''


# 问题描述： 给定一个整型数组A， 以及整数M，判断A中是否包含这样的i，j
# ，使得M = A[i] + A[j]

# 1 暴力枚举法
# 不用考虑先排序
# 算法升级： 如果存在则返回两个数的下标
'''
A = [1,2,3,4,5,6]
#A =[1,2]
M = 10
success = False
a = 0
b = 0
for i in A:
   # print("i:",i)
    for j in A:
        if i != j:
           # print('j:',j)
            if (i + j) == M:
                success = True
                a = i
                b = j
                    
print(a, b, success)
'''

# 折中查找，也叫二分查找
# 根据实际测试，只能看能否找到这个数，不能返回正确的下标，需要重新设计
def binaryFind(A, m):
    if len(A) == 0:
        return -1
    
    i = len(A)//2
   # print(i)

    if A[i] == m:
        return A[i]
    if A[i] > m and i - 1 >= 0:
        return binaryFind(A[0:i], m)
    if A[i] < m and i + 1 < len(A):
        return binaryFind(A[i: len(A)], m)

    return -1
A = [3, 1, 5, 6, 7, 4, 2, 8]
m = 1
# 把A按升序排列
A.sort()
#print(binaryFind(A,m))

# print(A)
success  = False
#A =[2,6]
M = 11
for i in A:
    m = M - i
    j = binaryFind(A, m)
    if j != -1 and j != i:
        print('存在i和j使得A[i] + A[j] = {}'.format(M))
        success = True
        break
if not success:
    print('不存在i和j使得A[i] + A[j] = {}'.format(M))
    



                

