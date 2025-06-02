# ctrl + alt + l(格式快捷键)
# Ctrl + / (注释快捷键)
# python一切皆为对象
# 显示类型转换注意事项
from contextlib import nullcontext

# 1.不管是str,float都可以转化成str,str(x)将x转换成字符串
n1 = 100
n2 = 100.02

print(str(n1))
print(str(n2))

# int 转变成float时，会增加小数部分；比如123（int）转换成float时，123会变成123.0
# float转变成整数int，123.65->123，小数部分会被删掉

print(float(n1))  # 100.00
print(int(n2))  # 100

# str转int，float（x）转int
n3 = "123.3"#“123.3”是str类型
n4 = nullcontext
print("n4=", float(n3), type(n4))
#print(int(n3)) #报错，因为不知道如何将str里面的内容“123.3”转换成123.3或者1233
'''进行格式转换时，要确保被转换的代码形式正确，比如123可以转换成整数，但不能将hello转换成整数
如果转换格式不正确，就会报错-- valueError，程序终止
n5 = hello
print(float(n5)) //n5是float类型，不能转换成float类型
print(int(n5)) //n5是str类型，不能转换成int类型
'''

# 对一个数据进行强制转换，会返回一个数据/值。强制转换后，并不会改变原来变量的数据类型（不会改变原变量所指的数据/值的数据类型）
# 系统会开辟新的变量进行存放比如
i = 10
j = float(i)
print("i的值：", i, "i的类型：", type(i))  # 10,int
print("j的值：", j, "j的类型：", type(j))  # 10.0,float
k = str(i)
print("k的值：", k, "k的类型：", type(i))  # "10",str
