# 蓝桥杯校内模拟赛第一期

# 一、填空题

## ① 二进制位数

* 问题描述
  * 十进制整数 2 在十进制中是 1 位数，在二进制中对应 10 ，是 2 位数。
  * 十进制整数 22 在十进制中是 2 位数，在二进制中对应 10110 ，是 5 位数。
  * 请问十进制整数 2022 在二进制中是几位数？
* 解：2022 —— 11111100110
* 答案：11

### 编码

```py
print(len(bin(2022))-2)
```

## ② 晨跑

* 问题描述
  * 小蓝每周六、周日都晨跑，每月的 1、11、21、31日也晨跑。其它时间不晨跑。
  * 已知 2022年1月1日是周六，请问小蓝整个2022年晨跑多少天？
* 答案：138

### 编码

```py
# -*- coding: utf-8 -*-
import datetime

start = datetime.datetime(year=2022, month=1, day=1)  # 定义头为2022.1.1
end = datetime.datetime(year=2023, month=1, day=1)  # 尾为2023.1.1
cnt = 0  # 计数
while start != end:  # 当没到下一年的时候，也就是遍历2022全年
    if start.isoweekday() in [6, 7] or start.day in [1, 11, 21, 31]:
        cnt += 1  # 小蓝每周六、周日都晨跑，每月的 1、11、21、31日也晨跑。
    start += datetime.timedelta(days=1)  # 下一天

print(cnt)
```

## ③ 调和级数

* 问题描述
  * 小蓝特别喜欢调和级数 S(n)=1/1+1/2+1/3+1/4+...+1/n 。
  * 请问，n 至少为多大时，S(n)>12 ？
* 答案：91380

### 编码

```python
# -*- coding: utf-8 -*-

s = 0
i = 1
while s <= 12:
    s += 1.0/i
    i += 1
print(i-1) # 不用加最后一次
```

## ④ 山谷

* 问题描述
  * 给定一个字母矩阵，如果矩阵中的某个位置不在四条边上，而且该位置上的字母小于其上下左右四个位置的字母，则称为一个山谷。
  * 例如，对于如下矩阵


```c
DDDDD
CADCE
FFFFA
```
* 共有两个山谷，位于第二行第二列和第四列。请注意第二行第三列和第三行第五列都不是山谷。

  * 对于如下30行60列的字母矩阵（请用等宽字体查看），请问有多少个山谷？

```c
    PHQGHUMEAYLNLFDXFIRCVSCXGGBWKFNQDUXWFNFOZVSRTKJPREPGGXRPNRVY
　　STMWCYSYYCQPEVIKEFFMZNIMKKASVWSRENZKYCXFXTLSGYPSFADPOOEFXZBC
　　OEJUVPVABOYGPOEYLFPBNPLJVRVIPYAMYEHWQNQRQPMXUJJLOOVAOWUXWHMS
　　NCBXCOKSFZKVATXDKNLYJYHFIXJSWNKKUFNUXXZRZBMNMGQOOKETLYHNKOAU
　　GZQRCDDIUTEIOJWAYYZPVSCMPSAJLFVGUBFAAOVLZYLNTRKDCPWSRTESJWHD
　　IZCOBZCNFWLQIJTVDWVXHRCBLDVGYLWGBUSBMBORXTLHCSMPXOHGMGNKEUFD
　　XOTOGBGXPEYANFETCUKEPZSHKLJUGGGEKJDQZJENPEVQGXIEPJSRDZJAZUJL
　　LCHHBFQMKIMWZOBIWYBXDUUNFSKSRSRTEKMQDCYZJEEUHMSRQCOZIJIPFION
　　EEDDPSZRNAVYMMTATBDZQSOEMUVNPPPSUACBAZUXMHECTHLEGRPUNKDMBPPW
　　EQTGJOPARMOWZDQYOXYTJBBHAWDYDCPRJBXPHOOHPKWQYUHRQZHNBNFUVQNQ
　　QLRZJPXIOGVLIEXDZUZOSRKRUSVOJBRZMWZPOWKJILEFRAAMDIGPNPUUHGXP
　　QNJWJMWAXXMNSNHHLQQRZUDLTFZOTCJTNZXUGLSDSMZCNOCKVFAJFRMXOTHO
　　WKBJZWUCWLJFRIMPMYHCHZRIWKBARXBGFCBCEYHJUGIXWTBVTREHBBCPXIFB
　　XVFBCGKCFQCKCOTZGKUBMJRMBSZTSSHFROEFWSJRXJHGUZYUPZWWEIQURPIX
　　IQFLDUUVEOOWQCUDHNEFNJHAIMUCZFSKUIDUBURISWTBRECUYKABFCVKDZEZ
　　TOIDUKUHJZEFCZZZBFKQDPQZIKFOBUCDHTHXDJGKJELRLPAXAMCEROSWITDP
　　TPCCLIFKELJYTIHRCQAYBNEFXNXVGZEDYYHNGYCDRUDMPHMECKOTRWOSPOFG
　　HFOZQVLQFXWWKMFXDYYGMDCASZSGOVSODKJGHCWMBMXRMHUYFYQGAJQKCKLZ
　　NAYXQKQOYZWMYUBZAZCPKHKTKYDZIVCUYPURFMBISGEKYRGZVXDHPOAMVAFY
　　RARXSVKHTQDIHERSIGBHZJZUJXMMYSPNARAEWKEGJCCVHHRJVBJTSQDJOOTG
　　PKNFPFYCGFIEOWQRWWWPZSQMETOGEPSPXNVJIUPALYYNMKMNUVKLHSECDWRA
　　CGFMZKGIPDFODKJMJQWIQPUOQHIMVFVUZWYVIJGFULLKJDUHSJAFBTLKMFQR
　　MYJFJNHHSSQCTYDTEAMDCJBPRHTNEGYIWXGCJWLGRSMEAEARWTVJSJBAOIOJ
　　LWHYPNVRUIHOSWKIFYGTYDHACWYHSGEWZMTGONZLTJHGAUHNIHREQGJFWKJS
　　MTPJHAEFQZAAULDRCHJCCDYRFVVRIVUYEEGFIVDRCYGURQDREDAKUBNFGUPR
　　OQYLOBCWQXKZMAUSJGMHCMHGDNMPHNQKAMHURKTRFFACLVGRZKKLDACLLTEO
　　JOMONXRQYJZGINRNNZWACXXAEDRWUDXZRFUSEWJTBOXVYNFHKSTCENAUMNDD
　　XFDMVZCAUTDCCKXAAYDZSXTTOBBGQNGVVPJGOJOGLMKXGBFCPYPCKQCHBDDZ
　　WRXBZMQRLXVOBTWHXGINFGFRCCLMZNMJUGWWBSQFCIHUBSJOLLMSQSGHMCPH
　　ELSOTFLBGSFNPCUZSRUPCHYNVZHCPQUGRIWNIQXDFJPWPXFBLKPNPEELFJMT
```
* 答案：276

### 编码

```python
# -*- coding: utf-8 -*-

m = '''PHQGHUMEAYLNLFDXFIRCVSCXGGBWKFNQDUXWFNFOZVSRTKJPREPGGXRPNRVY
STMWCYSYYCQPEVIKEFFMZNIMKKASVWSRENZKYCXFXTLSGYPSFADPOOEFXZBC
OEJUVPVABOYGPOEYLFPBNPLJVRVIPYAMYEHWQNQRQPMXUJJLOOVAOWUXWHMS
NCBXCOKSFZKVATXDKNLYJYHFIXJSWNKKUFNUXXZRZBMNMGQOOKETLYHNKOAU
GZQRCDDIUTEIOJWAYYZPVSCMPSAJLFVGUBFAAOVLZYLNTRKDCPWSRTESJWHD
IZCOBZCNFWLQIJTVDWVXHRCBLDVGYLWGBUSBMBORXTLHCSMPXOHGMGNKEUFD
XOTOGBGXPEYANFETCUKEPZSHKLJUGGGEKJDQZJENPEVQGXIEPJSRDZJAZUJL
LCHHBFQMKIMWZOBIWYBXDUUNFSKSRSRTEKMQDCYZJEEUHMSRQCOZIJIPFION
EEDDPSZRNAVYMMTATBDZQSOEMUVNPPPSUACBAZUXMHECTHLEGRPUNKDMBPPW
EQTGJOPARMOWZDQYOXYTJBBHAWDYDCPRJBXPHOOHPKWQYUHRQZHNBNFUVQNQ
QLRZJPXIOGVLIEXDZUZOSRKRUSVOJBRZMWZPOWKJILEFRAAMDIGPNPUUHGXP
QNJWJMWAXXMNSNHHLQQRZUDLTFZOTCJTNZXUGLSDSMZCNOCKVFAJFRMXOTHO
WKBJZWUCWLJFRIMPMYHCHZRIWKBARXBGFCBCEYHJUGIXWTBVTREHBBCPXIFB
XVFBCGKCFQCKCOTZGKUBMJRMBSZTSSHFROEFWSJRXJHGUZYUPZWWEIQURPIX
IQFLDUUVEOOWQCUDHNEFNJHAIMUCZFSKUIDUBURISWTBRECUYKABFCVKDZEZ
TOIDUKUHJZEFCZZZBFKQDPQZIKFOBUCDHTHXDJGKJELRLPAXAMCEROSWITDP
TPCCLIFKELJYTIHRCQAYBNEFXNXVGZEDYYHNGYCDRUDMPHMECKOTRWOSPOFG
HFOZQVLQFXWWKMFXDYYGMDCASZSGOVSODKJGHCWMBMXRMHUYFYQGAJQKCKLZ
NAYXQKQOYZWMYUBZAZCPKHKTKYDZIVCUYPURFMBISGEKYRGZVXDHPOAMVAFY
RARXSVKHTQDIHERSIGBHZJZUJXMMYSPNARAEWKEGJCCVHHRJVBJTSQDJOOTG
PKNFPFYCGFIEOWQRWWWPZSQMETOGEPSPXNVJIUPALYYNMKMNUVKLHSECDWRA
CGFMZKGIPDFODKJMJQWIQPUOQHIMVFVUZWYVIJGFULLKJDUHSJAFBTLKMFQR
MYJFJNHHSSQCTYDTEAMDCJBPRHTNEGYIWXGCJWLGRSMEAEARWTVJSJBAOIOJ
LWHYPNVRUIHOSWKIFYGTYDHACWYHSGEWZMTGONZLTJHGAUHNIHREQGJFWKJS
MTPJHAEFQZAAULDRCHJCCDYRFVVRIVUYEEGFIVDRCYGURQDREDAKUBNFGUPR
OQYLOBCWQXKZMAUSJGMHCMHGDNMPHNQKAMHURKTRFFACLVGRZKKLDACLLTEO
JOMONXRQYJZGINRNNZWACXXAEDRWUDXZRFUSEWJTBOXVYNFHKSTCENAUMNDD
XFDMVZCAUTDCCKXAAYDZSXTTOBBGQNGVVPJGOJOGLMKXGBFCPYPCKQCHBDDZ
WRXBZMQRLXVOBTWHXGINFGFRCCLMZNMJUGWWBSQFCIHUBSJOLLMSQSGHMCPH
ELSOTFLBGSFNPCUZSRUPCHYNVZHCPQUGRIWNIQXDFJPWPXFBLKPNPEELFJMT'''

matrix = m.split('\n')
cnt = 0
for i in range(1,29):
    for j in range(1,59):
        if matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j+1] and matrix[i][j] < matrix[i][j-1]:
            cnt += 1
print(cnt)
```

## ⑤ 最小矩阵

* 问题描述
  * 小蓝有一个 100 行 100 列的矩阵，矩阵的左上角为 1。其它每个位置正好比其左边的数大 2，比其上边的数大 1 。
  * 例如，第 1 行第 2 列为 3，第 2 行第 2 列 为 4，第 10 行第 20 列为 48。
  * 小蓝想在矩阵中找到一个由连续的若干行、连续的若干列组成的子矩阵，使得其和为 2022，请问这个子矩阵中至少包含多少个元素（即子矩阵的行数和列数的乘积）。
* 答案：12

### 编码

```python
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
```

# 二、编程题

## ⑥ 核酸

* 问题描述
  * ![image-20221113184147663](http://qny.expressisland.cn/schoolOpens/image-20221113184147663.png)

### 编码

```python
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

a = int(input())
b = int(input())

if b>a:
    print(b - a)
else:
    print(b + 7 - a)
```

## ⑦ 英文转换

* 问题描述
* ![image-20221113190251593](http://qny.expressisland.cn/schoolOpens/image-20221113190251593.png)

### 编码

```python
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

s = raw_input()
res = ''
for i in s:
    if i in "aeiou":
        res += i.upper() # 转化为大写
    else:
        res += i
print(res)
```

## ⑧ 充电器

* 问题描述
* ![image-20221113194833955](http://qny.expressisland.cn/schoolOpens/image-20221113194833955.png)
* ![image-20221113194844081](http://qny.expressisland.cn/schoolOpens/image-20221113194844081.png)

### 编码

```python
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
```

## ⑨ 全相等三角形

* 问题描述
* ![image-20221113195141696](http://qny.expressisland.cn/schoolOpens/image-20221113195141696.png)
* ![image-20221113195152330](http://qny.expressisland.cn/schoolOpens/image-20221113195152330.png)
* ![image-20221113195209373](http://qny.expressisland.cn/schoolOpens/image-20221113195209373.png)

### 编码

```python
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
```

## ⑩ 最小下标

* 问题描述
* ![image-20221113195609883](http://qny.expressisland.cn/schoolOpens/image-20221113195609883.png)
* ![image-20221113195620802](http://qny.expressisland.cn/schoolOpens/image-20221113195620802.png)

### 编码

```python
不会，摆烂了
```

