#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime

start = datetime.date(2000,1,1)
end = datetime.date(2020,10,1)
days = datetime.timedelta(days=1)
km =0

while end >=start:
  if start.day == 1 or start.weekday() ==0:
    km +=2
  else:
    km +=1
  start += days

print(km)     #8879

# 题目描述
# 本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。
#
# 小蓝每天都锻炼身体。
#
# 正常情况下，小蓝每天跑 11 千米。如果某天是周一或者月初（11 日），为了激励自己，小蓝要跑 22 千米。如果同时是周一或月初，小蓝也是跑 22 千米。
#
# 小蓝跑步已经坚持了很长时间，从 20002000 年 11 月 11 日周六（含）到 20202020 年 1010 月 11 日周四（含）。请问这段时间小蓝总共跑步多少千米？
#
# 运行限制
# 最大运行时间：1s
# 最大运行内存: 128M
