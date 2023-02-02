# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from re import L

n, m = map(int, raw_input().split())

M = []
for _ in range(n):
    M.append(raw_input())

ans = 0  # 计数 LQ三角形


# 定义函数，查看是否是LQ三角形，一共有四种
# 因为一共有4个方向，两两相邻的组合，一共是四种情况
def check(x, y, a, b, d):
    if d == 0:
        # _|的情况
        # x,y 为左顶点
        # a,b 为上顶点
        while x >= a and y <= b:
            if M[a][b] != M[x][y]: return False
            x -= 1
            y += 1
    elif d == 1:
        # |_的情况
        # x,y 为右顶点
        # a,b 为上顶点
        while x >= a and y >= b:
            if M[a][b] != M[x][y]: return False
            x -= 1
            y -= 1
    elif d == 2:
        # -|的情况
        # x,y 为左顶点
        # a,b 为下顶点
        while x <= a and y <= b:
            if M[a][b] != M[x][y]: return False
            x += 1
            y += 1
    elif d == 3:
        # |-的情况
        # x,y 为右顶点
        # a,b 为下顶点
        while x <= a and y >= b:
            if M[a][b] != M[x][y]: return False
            x += 1
            y -= 1

    return True


for i in range(n):
    for j in range(m):
        up, down, left, right = 0, 0, 0, 0
        # 得到上下左右相等的最大的数，利用四个while循环
        while (i - up) >= 0 and M[i][j] == M[i - up][j]:
            up += 1
        while (i + down) < n and M[i][j] == M[i + down][j]:
            down += 1
        while (j - left) >= 0 and M[i][j] == M[i][j - left]:
            left += 1
        while (j + right) < m and M[i][j] == M[i][j + right]:
            right += 1
            # _|的情况
        for k in range(1, min(up, left)):
            # 左顶点坐标(i,j-k),上顶点坐标(i-k,j)
            if check(i, j - k, i - k, j, 0):
                ans += 1

        # |_的情况
        for k in range(1, min(up, right)):
            # 右顶点坐标(i,j+k),上顶点坐标(i-k,j)
            if check(i, j + k, i - k, j, 1):
                ans += 1
        # -|的情况
        for k in range(1, min(down, left)):
            if check(i, j - k, i + k, j, 2):
                ans += 1
        # |-的情况
        for k in range(1, min(down, right)):
            if check(i, j + k, i + k, j, 3):
                ans += 1

print(ans)







