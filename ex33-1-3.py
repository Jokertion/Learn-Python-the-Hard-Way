i = 0 
numbers = []
maxium = int(input("请输入列表最大值： "))
step = int(input("请定义数字间隔（范围1-10）： "))

while i < maxium:
	print ("At the top i is %d" % i)
	numbers.append(i)	
	i += step
	print ("Numbers now: ", numbers)
	print ("At the bottom i is %d" % i)

print ("The numbers: ")

for num in numbers:
	print (num)