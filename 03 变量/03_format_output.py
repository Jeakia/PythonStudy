#格式化输出

#按照指定格式按照内容输出
#1.%操作符
#2.format()函数
#3.f-strings

name = "陈子佳"
age = 15
gender = "男"
score = 80.5

#格式化输出
#string 字符串

print("个人信息：%s-%d-%s 成绩：%.2f" %(name,age,gender,score))
#print("个人信息：%s-%d-%s 成绩：%.2f" %(age,name,gender,score))
# %d format: a real number is required, not str 报错


#format()
#print("个人信息：{} {} {} {}".format(name,age,gender))
#Replacement index 3 out of range for positional args tuple 报错

#f-strings
print(f"个人信息：{name} {age} {score} {gender}")
#要先定义，再使用。不能出现没有定义过的变量
#用f，编译器可以用将{}里面的内容当做变量
