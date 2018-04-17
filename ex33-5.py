i = 0 
numbers = []
maxium = int(input("请输入列表最大值： "))
step = int(input("请定义数字间隔（范围1-10）： "))


for loop in range(0, maxium, step):
	numbers.append(i)
	i = i + step

print ("The numbers: ")

for num in numbers:
	print (num)