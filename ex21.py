#定义方法：加
def add(a, b):					
	print ("ADDING %d + %d" % (a, b))
	return a + b
	
#定义方法：减
def subtract(a,b):
	print ("SUBTRACTING %d - %d" %(a, b))
	return a - b
	
#定义方法：乘
def multiply(a, b):
	print ("MULTIPLYING %d * %d" %(a, b))
	return a * b
	
#定义方法：除	
def divide(a, b):
	print ("DEVIDING %d / %d" % (a, b))
	return a / b
	
print ("Let's do some math with just fuctions!")
#加减乘除函数的调用，并带入数字
age = add(30, 5)
height = subtract(78, 4)
weight = multiply (90, 2)
iq = divide(100, 2)

#打印变量数值
print ("Age: %d, Height: %d, Weight:%d, IQ: %d" % (age, 
	height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
print ("Here is a puzzle.")

what = add(age, subtract(height,multiply(weight,divide(iq,2))))

print ("That becomes: ", what, "Can you do it by hand?")


#附加题
#1.如果你不是很确定return的功能，尝试自己写几个函数出来，让它们返回一些值。
#  你可以将任何可以放在=右边的东西作为一个函数的返回值。

#2.这个脚本的结尾是一个迷题。我将一个函数的返回值用作了另外一个函数的参数。
#  我将它们连接一起，就像写数学等式一样。这样可能有些难懂，不过运行一下你就知道结果了。
#  你可以试试看能不能用正常的方法实现和这个表达式一样的功能。

#3.一旦你解决了这个迷题，试着修改一下函数里的某些部分，然后看会有什么样的结果。
#  你可以有目的地修改它，让它输出另外一个值。

#4.颠倒过来再做一次。写一个简单的等式，使用相同的函数来计算它。




