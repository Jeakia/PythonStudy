#3 数值类型
#3.1 int整型（常用）：任意大小的整数
num = 10000
#检测数据类型的方法 type()
print(type(num))

#3.2 float 浮点型：小数
num2 = 1.5
print(type(num2))

#3.3 bool型（重点） 通常用于判断
#有固定写法：一个为true, 一个为false
print(type(True)) # True 和 False必须严格区分大小写

#bool值可以当作整形对待, True相当于整数1 False相当于整数0
print(True + False) #1+0=1
print(True + 1)

#3.4 complex 复数型 #j是固定形式--代表虚数，不能改成其他的字母
#固定写法：z=a + bj  -- a是实部，b是虚部，j是虚数单位
print(type(2+3j))
ma = 1+2j
ma2 = 2 + 3j
print(ma+ma2)

#4.1 字符串str
#特点： 需要加上引号，单引号和双引号都是可以的，包括了多行内容的时候也可以使用三引号
#name = sixstar 没有引号，被识别成变量名，sixstar没有被赋值，所以这个变量没有被创建
name = 'sixstar'
name = ("sixstar")
name = ("""sixstar""")
print(name)
print(type(name))
"""我是注释，不会被执行""" #注意，多行注释和字符串用三引号字符串类型的区别，多行注释是单独存在，不需要变量名


#5.1 格式化输出：生成一定格式的字符串
#占位符
#占位符的三种方式
# 1.%
# 2.format()
# 3.格式化f

# %格式化
#1. %s 字符串（常用）
name = 'bingbing'
print("我的名字：%s" %name)
#注意：占位符只是占据位置，并不会输出内容

#2. %d 整数（常用）
# age = 18;
# name  = 'bingbing'
# print("我的名字：%s, 年龄：%d" %(name,age))
#整数设置位数，不足前面补空白
a = 123
print("%06d" %a)#表示输出的整数显示位数，不足的话用0不全，超过的话原样输出

#4. %f 浮点数（常用浮点数）
a=1.2345678
print("%f" %a)#默认后六位小数，并遵循四舍五入原则

#5. %.4f 浮点数
# 数字设置小数位数
b=2.34567
print("%.4f" %b) #遵循四舍五入原则
#默认显示七位小数

#6. %%占位符
print("我是%%的1%%" % ())

#5.3f格式化
#格式：f"(表达式)"
name="bingbing"
age=18
print(f"我的名字是{name},我今年{age}岁了")