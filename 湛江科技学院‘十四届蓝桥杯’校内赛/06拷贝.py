# -*- coding: utf-8 -*-
# 06拷贝
import sys
reload(sys)
sys.setdefaultencoding('utf8')

t = int(input())
c = int(input())
s = int(input())

speed = float(c/t)
sc = s-c
res = int(sc/speed)
print(res)
