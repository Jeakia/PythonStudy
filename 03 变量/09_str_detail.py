# 字符串使用注意事项
# 字符串中出现双引号有可能报错。需要进行修改

str1 = "tom说:\"hello\""
print(str1)

str2 = "jackie说：'你好'"
print(str2)

print(f"str1的类型是{type(str1)},str2的类型是{type(str2)}")

# 通过加号能够连接字符串
name = 'google ' + 'microsoft'
print(name)

# python不支持单字符类型，即单个字母也当做字符串类型来使用 而不是char类型
str3 = "a"
print()

# 用三个单引号'''内容'''，或者三个双引号"""内容"""，保持内容原样输出
content = '''
from abc import ABC

class MyABC(ABC):
    pass

    MyABC.register(tuple)

assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)

不管黑猫白猫，能抓老鼠都是好猫
'''
print(content)

# 在字符串前面加个r可以保证句子保留原样式输出
str4 = "king\nqueen\tsuperman"
str5 = r"king\nqueen\tsuperman"  # 字符串前加了个‘r’
print(str4)
print(str5)

# 讲解字符串的驻留机制
'''在cmd--python模式下'''

str1 = "hello"
str2 = "hello"
str3 = "hello"

# id()函数是，可以返回对象/数据的内存地址
print("str1的内存地址是：", id(str1))
print("str2的内存地址是：", id(str2))
print("str3的内存地址是：", id(str3))

# 字符串驻留机制运行模式
# 1.字符串是由26个字母大小写，0-9,_组成
# 2.若出现非上述的字符时，字符串驻留机制不会启动
# 3.字符长度为0或者1时
# 4.字符串在编译时进行驻留，而不是运行时
# 5.[-5,256]的整数数字


# 1.字符串是由26个字母大小写，0-9,_组成
a = "abcABC_123"
b = "abcABC_123"
print(id(a))
print(id(b))
# 2.若出现非上述的字符时，字符串驻留机制不会启动
a1 = "abcABC_123#"
b1 = "abcABC_123#"
print(id(a1))
print(id(b1))

# 3.字符长度为0或者1时
a2 = ""
b2 = ""
print(id(a2))
print(id(b2))

#4. 数字
a=-5
b=-5
print(id(a))
print(id(b))

a5=-6
b5=-6
print(id(a))
print(id(b))

'''
pycharm的字符串驻留机制进行优化，字符串相同时--地址相同；
'''

str1="123*"
str2="123*"
print(f"str1的地址是：{id(str1)}；str2的地址是：{id(str2)}。两者完全相同")

'''避免频繁的记录，节省内存空间，也方便清除'''
#cmd python
s1 = "123#"
s2 = "123#"
import sys
s2 = sys.intern(s1)
print(id(s1))
print(id(s2))#通过sys.intern命令将s2的id强转换得跟s1的id一致，不另开内存

