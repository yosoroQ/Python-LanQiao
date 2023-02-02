# -*- coding: utf-8 -*-
# 07单词
import sys
reload(sys)
sys.setdefaultencoding('utf8')

temp = []
list = []
t = int(input())

for i in range(t):
    list.append(input())
for j in range(t):
    if j not in temp:
        temp.append(input())
print(temp)

