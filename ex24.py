print ("Let's practice everything.")
#转义字符 \n换行 \t横向制表符
print ('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

#三引号 放入多行文字	
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print ("---------------")
print (poem)
print ("---------------")

#格式化 调用数字
five = 10 - 2 + 3 - 6
print ("This should be five: %s" % five)

#定义方法：最初值
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
start_point  = 10000
beans, jars, crates = secret_formula(start_point)

#格式化 调用参数
print ("With a starting point of: %d" % start_point)
print ("We'd have %d beans, %d jars, and %d crates."
	% (beans, jars, crates))
	
#格式化 调用函数
start_point = start_point / 10
print ("We can also do that this way:")
print ("We'd have %d beans, %d jars, and %d crates."
	% secret_formula(start_point))
	