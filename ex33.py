i = 0 
numbers = []

while i < 6:
	print ("At the top i is %d" % i)
	numbers.append(i)
	
	i = i + 1
	print ("Numbers now: ", numbers)
	print ("At the bottom i is %d" % i)
	
print ("The numbers: ")

for num in numbers:
	print (num)
#+++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++
"""
附加题
1.将这个while循环改成一个函数，将测试条件(i < 6)中的 6 换成一个变量。 
# maxium = int(input("请输入列表最大值： \n"))
# 把6替换成变量↓
# while i < maxium:

2.使用这个函数重写你的脚本，并用不同的数字进行测试。
OK

3.为函数添加另外一个参数，这个参数用来定义第 8 行的加值 +1 ，这样你就可以让它加任意值了。
# 添加了一个step变量

4.再使用该函数重写一遍这个脚本。看看效果如何。
OK

5.使用for-loop和range把这个脚本再写一遍。你还需要中间的加值操作吗？如果不去掉它，会有什么样的结果？
OK  for循环中可以使用in range(a,b,c) a->起始值，b->结束值，c->跨度（step）值，从而实现和本脚本一样的效果
for loop in range(0, maxium, step):
	numbers.append(i)
	i = i + step
	
很有可能你会碰到程序跑着停不下来了，这时你只要按着 CTRL 再敲 c (CTRL-c)，这样程序就会中断下来了。