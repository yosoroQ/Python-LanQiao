# -*- coding: utf-8 -*-
sum = 0
for i in range(1950,2022):
    if(i%4==0 and i%100 !=0) or i%400 ==0:
        sum += 366
    else:
        sum += 365
sum=sum+31+30+31
print(sum)

