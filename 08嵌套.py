#列表嵌套字典
# zhangsan = [ {'height':170,'age':29}, {'movie':'science fiction','play':'football'}, 'single' ]
# print(zhangsan)
# print(zhangsan[0],'\t',zhangsan[1],'\t',zhangsan[-1])
# print(zhangsan[-2]['play'])   #类似c中的二元数组
#字典嵌套列表
zhangsan_fav = {'movie':['science fiction','action','war'],'play':'football'}
print(zhangsan_fav)
print(zhangsan_fav['play'])
print(zhangsan_fav['movie'][1])
#字典嵌套字典
zhangsan_1 = {'a':{'b':'c','d':2},'e':'f'}
print(zhangsan_1)
print(zhangsan_1['a'])
print(zhangsan_1['a']['d'])
#列表嵌套列表
zhangsan_2 = ['a','b','c',['d','e','f']]
print(zhangsan_2)
print(zhangsan_2[1])
print(zhangsan_2[-1][1])