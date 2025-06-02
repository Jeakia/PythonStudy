i = 10
j = float(i) #10.0

print(type(i)) #int
print(type(j)) #float

#注意！！！
i = j + 1 #11.0 是float类型，向高精度转换，所以i是float类型了，是11.0
print(type(i)) #float
print(type(j)) #float

print(i) #11.0
print(int(i)) #11
print(type(i)) #int 错误！！！ 是float类型，这里的转换语句跟原来上文的i没有影响
