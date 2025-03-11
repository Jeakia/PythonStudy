#讲解int类型的细节
#在python中，int可以表达很大的数
import sys

# n3 = 9 ** 8888
# print("n3 =",n3,type(n3))
#ValueError: Exceeds the limit (4300 digits) for integer string conversion;
#python数字可以存放4300个，超过会报错

#oct 八进制；bin 二进制；dec 十进制；hex 十六进制
#python的整数有十进制，十六进制，八进制，二进制
#int 十进制最常见的写法：1,66,128

# 十进制
print(10) #10
# 十六进制
print(0x10) #16
# 八进制
print(0o10) #8
# 二进制
print(0b10) #2

#python中的整形占多少个字节

# 字节(byte):计算机中基本存储单元
# 位(bit)计算机中最小的存储单元
# 1 byte（字节） = 8 bit （位）

n1 = 0
n2 = 1
n3 = 2
n4 = 2 ** 15
n5 = 2 ** 30
n6 = 2 ** 128
#在python中，可以通过sys.getsizeof，返回对象（数据）的大小（按照字节单位返回）

print(n1,sys.getsizeof(n1),"类型",type(n1))
print(n2,sys.getsizeof(n2),"类型",type(n2))
print(n3,sys.getsizeof(n3),"类型",type(n3))
print(n4,sys.getsizeof(n4),"类型",type(n4))
print(n5,sys.getsizeof(n5),"类型",type(n5))
print(n6,sys.getsizeof(n6),"类型",type(n6))




