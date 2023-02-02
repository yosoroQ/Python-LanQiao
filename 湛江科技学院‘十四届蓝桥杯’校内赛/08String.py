# -*- coding: utf-8 -*-
# # 08
def check(str):
    if (str == str[::-1]):
        return 1
    else:
        return 0


def reverse(str):
    a = list(str)
    a.reverse()
    return (''.join(a))


str = input("输入字符串:")
res = []
temp = []
n = len(str)

if n == 1:
    res = str
else:
    if (check(str)):
        res = str
    else:
        temp = list(str)
        # print(temp)
        for i in range(n):
            Str = str
            Str += reverse(temp[0:i + 1])
            # print("Str", Str)
            if (check(Str)):
                res = Str
                break
print(res)
