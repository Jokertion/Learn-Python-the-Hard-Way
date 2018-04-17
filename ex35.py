from sys import exit 

def gold_room():
	print ("This room is full of gold. How much do you take?")
	
	choice = input ("> ")
	#原判断代码：
    # if "0" in next or "1" in next:
    #     how_much = int(next)
    # else:
    #     dead("Man, learn to type a number.")
    #新增的判断，使用try当int()报错时，提示输入错误，否则进入对数字大小的判断

	try:
		how_much = int(choice)
	except:
		dead("Wrong input. Man, learn to type a number")
		
	if how_much < 50:
		print ("Nice, you're not greedy, you win!")
		exit(0)
	else:
		dead("You greedy bastard!")
		
def bear_room():
	print ("There is a bear here.")
	print ("The bear has a bunch of honey.")
	print ("The fat bear is in front of another door.")
	print ("How are you going to move the bear?")
	bear_moved = False
	#while True: 无限循环
	#and not bear_moved 使用非常巧妙。and 都为真才执行
	while True: 
		choice = input ("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		#调戏熊一次，bear_moved的值重新赋值为True，继续重复while循环
		elif choice == "taunt bear" and not bear_moved:
			print (" The bear has moved from the door. You can go through it now.")
			bear_moved = True 
		#要再次调戏熊，必须吃了你的腿
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print ("I got no idea what that means.")
			
def cthulhu_room():
	print ("Here you see the great evil Cthulhu.")
	print ("He, it, whatever stares at you and you go insane.")
	print ("Do you flee for your life or eat your head?")
	
	choice = input("> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
def dead(why):
	print (why, "Good job")
	exit(0)
	
def start():
	print ("You are in a dark room.")
	print ("There is a door to your right and left.")
	print ("Which one do you take?")

	choice = input ("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
	
start()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
附加题
1.把这个游戏的地图画出来，把自己的路线也画出来。
OK
2.改正你所有的错误，包括拼写错误。
OK 
3.为你不懂的函数写注释。
4.为游戏添加更多元素。通过怎样的方式可以简化并且扩展游戏的功能呢？

5.这个gold_room游戏使用了奇怪的方式让你键入数字。这种方式会导致什么样的 bug？
 你可以用比检查0、1更好的方式判断输入是否是数字吗？int() 这个函数可以给你一些头绪
 try:
        how_much = int(choice)
    except:
        dead("Wrong input. Man, learn to type a number")
 """
		