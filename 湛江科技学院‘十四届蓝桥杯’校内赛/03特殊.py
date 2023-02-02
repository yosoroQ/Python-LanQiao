# def six(number):
#     long = len(str(number))
#     l = []
#     num = 0
#     for i in range(1, long + 1):
#         num = number % 10
#         l.append(num)
#         number = int(number / 10)
#     result = 0
#     for i in range(0, long):
#         result = result + l[i] * pow(16, i)
#     return result
#
#
# for i in range(10, 10000):
#     res = six(i)
#     if res % i == 0:
#         print(i)
#         break

i = 10
while True:
    h = int(str(i), 16)  # 算出16进制的数
    if h % i == 0:
        print(i)
        break
i += 1
