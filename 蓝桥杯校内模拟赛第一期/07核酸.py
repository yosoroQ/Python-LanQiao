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