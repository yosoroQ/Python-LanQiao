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





