from sys import argv 								#引用

script, filename = argv     						#获取文件名
print ("We're going to erase %r." %filename)		#提示清除文件
print ("If you don't want that, hit CRRL-C(^C).")	#不想清除，按键提示
print ("if you do want that, hit RETURN.")			#想清除，按键提示

input("?")											#？+用户输入

print ("Opening the file...")						#提示正在打开文件
target = open(filename, 'w')						#打开文件

print ("Truncating the file. Goodbye!")				#正在清空文件
target.truncate()									#清空文件

print ("Now I'm going to ask you for three lines.")	#提示输入三行文字

print ("I'm going to write these to the file.")		#提示正在写入文件

target.write(input("line 1: "))									#第一行写入
target.write("\n")									#回车
target.write(input("line 2: "))								
target.write("\n")
target.write(input("line 3: "))
target.write("\n")

print ("And finally, we close it.")					#提示关闭
target.close()										#关闭




