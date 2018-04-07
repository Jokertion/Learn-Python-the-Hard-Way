x = "There are %d types of people." % 10    # %d 数字格式化
binary = "binary"							# 赋值binary 字符串	 
do_not = "don't" 							# 赋值do_not 字符串
y = "Those who know %s and those who %s."% (binary,do_not)  #多个格式化，后加逗号

print (x) 									# 输出字符串	
print (y)									# 输出字符串

print ("I said: %r." % x)					# %r 显示原始数据值
print ("I also said: '%s'. " % y)			# %s 显示输出的

hilarious = False 							# hilarious 赋布尔值 
joke_evaluation = "Isn't that joke so funny?! %r"  #joke_evaluation赋字符串，%r占位

print (joke_evaluation % hilarious)			# 输出 joke_evaluation， hilarious赋值%r

w = "This is the left side of..."			# 赋值w
e = "a sting with a right side."			# 赋值e

print (w + e) 								# 输出 w+e