# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

n = int(input())


# 将时间转化为秒数
def get_second(t):
    h, m, s = map(int, t.split(':'))  # 分别得到hour,minute,second
    return h * 3600 + m * 60 + s


T = []  # t储存所有的时间
for i in range(n):
    t, u, v = raw_input().split()  # 输入三个值
    u, v = int(u), int(v)
    t = get_second(t)
    T.append((t, u, v))

ans = 0
for i in range(n - 1):
    U, I = T[i][1], T[i][2]  # 电流和电压
    t = T[i + 1][0] - T[i][0]  # 时间差
    ans += U * I * t  # UIt
print(ans)





