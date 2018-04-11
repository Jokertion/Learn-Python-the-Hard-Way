from sys import  argv     			#引入参数变量

script, input_file = argv			#获取文件名		

def print_all(f):					#定义方法1：打印全部内容
	print (f.read())

def rewind(f):						#定义方法2：把指针指回文件的开始位置，
	f.seek(0)
	
def print_a_line(line_count, f):	#定义方法3：逐行打印行号和该行内容
	print (line_count,f.readline())
	
current_file = open(input_file)		#打开文件

print ("First let's print the whole file:\n")		#使用方法1：打印全部内容

print_all(current_file)								

print ("Now let's rewind, kind of like a tape.")	#使用方法2：把指针放到第一行

rewind(current_file)								

print ("Let's print three lines:")					#定义方法3：逐行打印行号和该行内容
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


#1.通读脚本，在每行之前加上注解，以理解脚本里发生的事情。
#ok
#2.每次print_a_line运行时，都传递了一个叫current_line的变量。在每次调用函数时，
#  打印出current_line的值，跟踪一下它在print_a_line中是怎样变成line_count的。

#3.找出脚本中每一个用到函数的地方。检查def一行，确认参数没有用错。

#4.上网研究一下file中的seek函数是做什么用的。试着运行pydoc file看看能不能学到更多。
# 参考：http://www.runoob.com/python3/python3-file-seek.html













