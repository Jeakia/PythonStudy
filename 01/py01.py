print("hello world")
#运行第一个py文件

print("hello python")
print("123")

#print("good evening") print("superman")
#SyntaxError 语法错误
#两个print不能写在同一行，错误信息中遇到SyntaxError，说明语法有问题

#命名错误 Nameerror
#name is not defiened 没有被定义

#run to cursor 跳到下一个断电的位置
#show exectuion point 显示执行的断点
#step into 下一步

#注释可以放在任意位置，但是注释的内容不会被程序执行
'''
我是多汗注释
print(123);
'''

"""
我也是多行注释
print(123);
"""

#多行注释是用三引号包含，可以是三对单引号，三对多引号

#快捷键，ctrl+/ 注释 可以添加，取消注释，使用的是单行注释
# ctrl+ d 复制到下一行

print(123);

# *value 值，表示可以一次输出多个对象。输出多个对象时，需要用，分开
#5.输出函数 print()
print("哈哈哈","hello","xixixi",sep='|') #sep只能放在语句后面。 sep就是用来间隔多个值
#输出多个值或者多句话时，需要用，隔开，英文模式下的。

#end:用来设定以...结尾，(默认值是\n，可以切换成其他字符串)
print("hello",end=" ")
print("bingbing")
#print(字符串,end="后面要拼接的值") 最后输出结果：第一个print字符串+后面拼接的值+第二个print中的字符串
