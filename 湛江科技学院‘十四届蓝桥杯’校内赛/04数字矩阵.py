a = []
with open('text.txt', 'r', encoding='UTF-8') as f:
    a = f.readlines()
f = [[0] * 70 for _ in range(70)]
for i in range(1, 31):
    for j in range(1, 61):
        if (i - 1) >= 0 and (j - 1) >= 0:
            f[i][j] = max(f[i - 1][j], f[i][j - 1]) + int(a[i - 1][j - 1])
        elif i - 1 >= 0:
            f[i][j] = f[i - 1][j] + int(a[i - 1][j - 1])
        elif j - 1 >= 0:
            f[i][j] = f[i][j - 1] + int(a[i - 1][j - 1])
print(f[30][60])

# 输出592