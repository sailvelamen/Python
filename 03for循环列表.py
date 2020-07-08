# name_age = ["zhangsan","lisi","wangma",'jia','yl','bin']

# for name in name_age :
#     print('Your name is: ',name)         #依次把列表中的元素赋值给name并打印出来
# print('输出结束')

# for x in range(1,10,3) :    #range()按规则生成数字range(开始，结束，间距)
#     print(x)

# numbers = list(range(1,10))   #把一串数字转换成列表
# print(numbers)

y = []
for x in range(1,10,2):    #for循环中的变量可以临时起
    y.append(x**2)
print(y)
            #列表解析
y = [x**2 for x in range(1,10,2)]    #range()的第一个数给x，x再给x**2(x的平方)
print(y)                             #然后x**2的值给y列表的第0个数在进行第二个循环

z1 = min(y)
print("y's min = ",z1)
z2 = max(y)
print("y's max = ",z2)
print("y's sum = ",sum(y))    #sum()只能处理列表