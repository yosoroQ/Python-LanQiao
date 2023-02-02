# -*- coding: utf-8 -*-


m = [[0]*100 for _ in range(100)]
for i in range(100):
    m[i][0] = i + 1 # 对于第一列来说，肯定是1,2,3,...100，因为第一个数为1，其他比上一行数大1
    for j in range(1,100):
        m[i][j] = m[i][j-1]+2 # 其左边的数大 2


# 取matrix[a:c][b:d]的子矩阵的和
def sum_matrix(a,b,c,d):
    ans = 0
    for i in range(a,c+1):
        for j in range(b,d+1):
            ans += m[i][j]
    return ans


res = float('inf') # res初始化为无穷小的数

for i in range(100):
    for j in range(100):
        for k in range(i,100):
            for z in range(j,100):
                ans = sum_matrix(i,j,k,z)
                if ans == 2022:
                    res = min(res,(k-i+1)*(z-j+1))
                    break
                elif ans > 2022:
                    break
print(res)


