# python变量在运行时根据它的上下文（即 当前值）决定
# 隐式类型转换 -- 也叫自动转换
var1 = 11
print(type(var1))  # int类型
var1 = 1.1
print(type(var1))  # float类型
var1 = "老陈"
print(type(var1))  # string类型

#运算的时候，数据类型会向 高精度 类型转换，float精度会高于int
var2 = 10 #int类型
var3 = 1.2 #float类型
var4 = var2 + var3 #11.2--float类型，int 向 float类型转换
print("var4=",var4,"var4的类型：",type(var4))
var2 = var2 + 0.1 #10.1赋值给了var2
print("var2=",var2,"var2的类型是：",type(var2))
#var2 进行了自动转换，字符类型从int转换到了float
#var2=10是int类型， + 0.1 = 10.1 var2变成了float类型了
#隐式类型转换