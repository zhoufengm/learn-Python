import calendar # 不能写 from calendar import calendar，会报错找不到month方法
import time
# python中时间日期格式化符号：

# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00-59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

localtime1 = time.localtime(time.time())
print('本地时间1： ',localtime1)


# 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
localtime = time.asctime(time.localtime(time.time()))
print('本地时间 ： ',localtime)

# 格式化日期
# time.strftime(format[, t])

# 格式化成2016-03-20 11:45:39形式
print( time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) )

# 格式化成Sat Mar 28 22:24:24 2016形式
# time.strftime(fmt[,tupletime])
# 接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定
print(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))

# 将格式字符串转换为时间戳
# time.mktime(tupletime)
# 接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）。
# time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
# 根据fmt的格式把一个时间字符串解析为时间元组。
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

# 获取某月日历
cal = calendar.month(2022,9)
print("以下输出2022年9月份的日历")
print(cal)

# calendar.calendar(year,w=2,l=1,c=6)
# 返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
cal2 = calendar.calendar(2022)
print('以下输出2022年历：')
print(cal2)

# calendar.isleap(year)
# 是闰年返回 True，否则为 False。
print('2020是否为闰年： ',calendar.isleap(2020))
print('2022是否为闰年： ',calendar.isleap(2022))

# calendar.leapdays(y1,y2)
# 返回在Y1，Y2两年之间的闰年总数。
print("1990和2022之间的闰年总数为：",calendar.leapdays(1990,2022))