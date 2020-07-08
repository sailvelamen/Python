# #布尔表达式：条件测试的别名
# print(3 == 4)
# print(3 == 3)  #python中可直接打印判断表达式的结果

# a = 'Lisi'
# b = 'zhangsan'
# c = 'lisi'
# print(a == b)
# print(a == c)    #python区分大小写
# print(a.lower() == c)
# print(a != b)
# print(a != c)

'''
x = 10; y = 20; z = 20; k = 10
print('x:',x,',y:',y,',z:',z,',k',k)
print('x == y: ',x == y)
print('y == z: ',y == z)
print('x>y: ',x>y)
print('x<y: ',x<y)
print('y >= z: ',y >= z)
print('y <= z: ',y <= z)
print('x == y and y == z: ',x == y and y == z)
print('x == k and y == z: ',x == k and y == z)
print('x == y or y == z:',x == y or y == z)
print('x == y or k == z:',x == y or k == z)
'''

# #检查特定值是否在列表中：in/not in
# names = ["zhangsan","lisi","wangma",'jia','yl','bin']
# print('zhangsan' in names)
# print('zhangsan' not in names)

#if语句：条件判断语句
# age = 14
# if age >= 18:
#     print('you are old enough to vote!')
# else:
#     print('sorry! you are too young!')

# age = 18
# if age<4:
#     print('your admission cost is $0.')
# elif age<18:
#     print('your admission cost is $5.')
# elif age>60:
#     print('your admission cost is $7.')
# else:
#     print('your admission cost is $10.') 

names = ["zhangsan","lisi","wangma",'jia','yl','bin']
name = 'zhangan'
# if name in names:
#     print('name is in names')
# else:
#     print('name is not  in names')

# names_2 = []
# if names_2:         #当变量没有赋值时用if判断不论怎么判断都是false
#     print("names_2")
# else:
#     print('nothing')        
for name in names:
    if name == 'lisi':
        print("lisi,go to school")
    elif name == 'bin':
        print('bin,go to school')