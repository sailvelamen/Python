#元组(tuple)：不可改变的列表

tuple_1 = (1,3,5,2,4,6,7,8,9)
print(tuple_1)
print('tuple_1[2]: ',tuple_1[2])

for x in tuple_1:
    print(x)

# tuple_1[3] = 100  #这样是修改不了的！！！！
# print(tuple_1) 

tuple_1 = (1,3,5,100,4,6,7,8,9)    #强制修改
print(tuple_1)