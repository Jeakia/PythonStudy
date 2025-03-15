# bool类型判断

num1 = 100
num2 = 200
# if num1 > num2: #如果这个条件成立，则返回以下句子
#     print("num1 > num2")

if num1 < num2:
    print("num1 < num2")

# bool类型
result = num1 > num2
# 把num1和num2的值赋给result这个变量
print("num1 > num2 is:", result)
print("result的类型是", type(result))  # 看result的类型

print(type(1 > -1))  # 也可以这样查看result的类型

# bool类型很多时候都跟“判断”相绑定比如：if
'''
bool类型只有 true和false两个类型
bool类型可以拿来跟其他类型进行比较如：数字和字符串或；
true为1； false为0；
在python中，非0为真值，0值为假值
'''
# 举例
print(True + 10)  # ?
print(False + 10)  # ?

b1 = True
b2 = False
if b1 == 1:
    print("yes")
if b2 == 0:
    print("hello")

# 非0是真值，0是假值
if 0:  # 假值，不输出morning
    print("morning")

if 1.1:
    print("no,it's afternoon")

if "of course":  # 把“of course”当做字符串，非0，是真值
    print("oh,yes. sorry")
