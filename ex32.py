# coding:utf-8
# ex32 循环和列表
# 这一课学习for循环和列表（list）

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#1.list可以储存数字类型
for number in the_count:
	print ("This is count %d" % number)

#2.list可以储存字符串类型
for fruit in fruits:
	print ("A fruits of type: %s" % fruit)

#3.list可以混合储存数字和字符串类型	
for i in change:
	print ("I got %r" %i)
	
#创建空列表	
elements = []

#以range限定for循环的范围，range()本身是个list，直接用list替代也有一样的效果如[1,2,3,4]等
for i in range(0, 6):
	print ("Adding %d to the list." %i)	
	#使用append可以向list的末尾添加一个元素
	elements.append(i)

#打印新建列表所有元素
for i in elements:
	print ("Element was: %d" % i)
	
"""	
1.注意一下range的用法。查一下 range 函数并理解它。

range() 函数可创建一个整数列表，一般用在 for 循环中。
函数语法:
range(start, stop[, step])
参数说明:
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

2.在第 22 行，你是否可以直接将elements赋值为range(0,6)，而无需使用 for 循环？

elements为list格式，range()也是list格式，所以不用for循环，可以直接用
elements = range(0,6)直接赋值

3.在 Python 文档中找到关于列表的内容，仔细阅读以下，除了 append 以外列表还支持哪些操作？
"""