#!usr/bin/python
#split()用法：指定分隔符对字符串进行切片
	"""
	 split()函数 
    语法：str.split(str="",num=string.count(str))[n] 
    参数说明： 
    str:表示为分隔符，默认为空格，但是不能为空('')。若字符串中没有分隔符，则把整个字符串作为列表的一个元素 
    num:表示分割次数。如果存在参数num，则仅分隔成 num+1 个子字符串，并且每一个子字符串可以赋给新的变量 
    [n]:表示选取第n个分片 
 
    注意：当使用空格作为分隔符时，对于中间为空的项会自动忽略 
	"""
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words 
	
#sort()用法：排序
	"""
    对List进行排序，sort是在原位重新排列列表，而sorted()是产生一个新的列表. 
    """
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

#pop（）用法：移除列表中的一个元素，并且返回该元素的值
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print (word)

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print (word)


def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

#定义方法：打印原始语句的首尾字符
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

#定义方法：打印排序的首尾字符	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
"""
1.研究答案中没有分析过的行，找出它们的来龙去脉。
确认自己明白了自己使用的是模块ex25中定义的函数。
OK
2.试着执行help(ex25)和help(ex25.break_words)。
这是你得到模块帮助文档的方式。 所谓帮助文档就是你定义函数时放在\"""之间的东西，
它们也被称作documentation comments （文档注解），后面你还会看到更多类似的东西。
OK
3.重复键入ex25. 是很烦的一件事情。有一个捷径就是用from ex25 import *的方式导入模组。
这相当于说：“我要把 ex25 中所有的东西 import 进来。
”程序员喜欢说这样的倒装句，开一个新的会话，看看你所有的函数是不是已经在那里了。
OK
4.把你脚本里的内容逐行通过python编译器执行，看看会是什么样子。
你可以通过输入quit()来退出Python。
"""
#Q: 什么情况下，我可以在函数中用print代替return？
"""
return是从函数给出的代码行调用的函数的结果。
你可以把函数理解成 通过参数获取输入，并通过return返回输出。
而print是与这个过程完全无关的，它只负责在终端打印输出。
"""