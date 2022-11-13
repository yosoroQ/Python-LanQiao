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
