# name_age = {'zhangsan':24,'lisi':26}  #定义字典
# #字典名          键    值(值也可以是字符串)   ==>键值对   
# print(name_age)
# print(name_age['lisi'])
# name_age['wangwu'] = 25   #在字典中添加键值对
# print(name_age)

# names_age_2 = {}
# print(names_age_2)
# names_age_2['zhaoliu'] = 29 
# print(names_age_2) 
# print('zhaoliu : ',names_age_2['zhaoliu'])
# names_age_2['zhaoliu'] = 92     #修改键值对
# print(names_age_2) 
# del names_age_2['zhaoliu']      #删除键值对
# print(names_age_2)

names_age = {'zhangsan':24,'lisi':5,'zhaoliu':29,'caojiu':29}
for key,value in names_age.items():      #(1)遍历字典
    print('\n',key,':',value)

for name in names_age.keys():   #(2)遍历字典显示所有键
    print(name)
print('\n')
for name in names_age.keys():    #遍历字典显示所有键值对
    print(name,names_age[name])
print('\n')
#字典没有索引号
for name in sorted(names_age.keys()):  #sorted()函数把字典中的所有键按字母顺序排序
    print(name,names_age[name])
print('\n')
for age in names_age.values():
    print(age)
print('\n')
for age in set(names_age.values()):  #set()函数去除重复元素
    print(age)
print('\n')

age_1 = [2,5,4,7,8,9,6,2,5,8,7,4,1,3]
print(set(age_1))
