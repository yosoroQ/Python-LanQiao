n, m = map(int, input().split())
M = []
for _ in range(n):
    M.append(input())
    cnt = 0
    x = min(n, m) // 2  # 最长的长度最大为min(n,m)//2,因为X是对称的
# 可以不遍历最外层一圈，因为单独一个字母不算x图形
for i in range(1, n - 1):
    for j in range(1, m - 1):
        # 遍历长度
        for k in range(1, x + 1):
            a, b, c, d = i - k, i + k, j - k, j + k
    if a >= 0 and b < n and c >= 0 and j < m:
        if M[i][j] == M[a][c] == M[b][c] == M[a][d] == M[b][d]:  # X 图形
            cnt += 1
        else:
            break
            print(cnt)
