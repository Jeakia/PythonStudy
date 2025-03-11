a = 100
#演示 type函数

name = "tom"
age = 20
score =  90.4
gender = "male"
is_pass = True

print(type(name))
print(type(age))
print(type(score))
print(type(gender))
print(type(is_pass))


#type可以直接看具体的（字面量）的值
print(f"hello的类型是{type('hello')} {type(123)} {type(89.54)}")
print(f"1.1的类型是{type(1.1)}")
print(f"89.65的类型是{type(89.65)}")
print(f"True的类型是{type(True)}")
