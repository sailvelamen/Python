y = [x for x in range(1,20,2)]
print(y)

print(y[1:5])    #切片
print(y[:3])
print(y[2:])
print(y[-4:])  #-4只是索引号，依旧从左向右

y_2 = y[:]     #复制列表  (在内存中单独开辟一个空间把y列表中的所有元素复制给y_2)
print('y_2:',y_2)
y_2.append(32)
y.append(442)
print('y:',y)
print('y_2',y_2)