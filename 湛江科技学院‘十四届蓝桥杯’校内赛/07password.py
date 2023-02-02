# -*- coding: utf-8 -*-
# 07单词
# temp = []
# list = []
# t = int(input())
#
# for i in range(t):
#     list.append(input())
# for j in range(t):
#     if j not in temp:
#         temp.append(list[j])
# print(temp)

# temp = []
# list = []
# n = int(input())
# for i in range(n):
#     list.append(input())
# for k in range(n):
#     if k not in temp:
#         temp.append(list[k])
# print(temp)

n = int(input())
words = []
for _ in range(n):
    word = input()
if word not in words:
    words.append(word)
print('\n'.join(words))