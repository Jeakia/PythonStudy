#显式类型转换
#如果需要对变量类型进行转化，只需要将数据类型作为函数名即可，这种类型就是显性转换/强制转换

'''案例'''

i = 10

j = float(i)#用float函数，将i变量的值转化成小数并且赋给了j，10变成了10.0
print("j的类型是：",type(j),"j = ",j)

k = str(i)
print("k的类型是：",type(k),"k = ",k) # str，“ 10"
# print(k+10)#报错，k是字符串类型，不能加int类型
# print(k+10)  #TypeError: can only concatenate str (not "int") to str 字符串
