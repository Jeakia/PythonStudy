n1 = 4.5
n2 = -3.6
print("n1 = ",n1)
print("n2 = ",n2)

#浮点数表示形式
# 十进制:0.512, .512

n3 = 5.12
n4 = .512
print("n4 = ",n4)

#科学计数法形式
n5 = 5.12e+2 #(5.12乘以10的2次方)
print("n5 = ",n5)

n6 = 5.12E-2
'''5.12除以10的2次方'''
print("n6 = ",n6)
'''comma是逗号'''

#浮点数有大小限制
#max=1.7976931348623157e+308
#min=2.2250738585072014e-308
#浮点类型计算后，会存在’精度损失‘的问题，可以使用Decimal类进行精确计算

#精度损失
'''
如何解决：为了避免浮点数的精度问题，可以使用Decimal类进行精确计算
2.如果使用decimal类，需要导入import Decimal类
'''
b = 8.1/3 #(2.7)
print("b =",b)#精度损失 返回2.66666...

#从decimal导入Decimal
from decimal import Decimal

b = Decimal("8.1") / Decimal("3")
print("b =",b)
#返回准确类型 2.7



