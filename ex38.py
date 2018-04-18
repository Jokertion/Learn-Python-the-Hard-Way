ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#pop()函数:移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
while len(stuff) != 10:
	next_one = more_stuff.pop()	
	print ("Adding: ", next_one)
	stuff.append(next_one)
	print ("There are %d items now." % len(stuff))
	
print ("There we go: ", stuff)

print ("Let's do some things with stuff.")

print (stuff[1])
print (stuff[-1]) # whao! fancy
print (stuff.pop())
print (' ' .join(stuff)) # what? cool!
print ('#'.join(stuff[3:5])) # super stellar!
#++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
附加题
1.将每一个被调用的函数以上述的方式翻译成 Python 实际执行的动作。比如more_stuff.pop() 是 pop(more_stuff).
stuff = ten_things.split(' ')	 	split(' '，ten_things)
next_one = more_stuff.pop()			pop(more_stuff)		
stuff.append(next_one)				append(next_one---》stuff)
print ('#'.join(stuff[3:5])) 		.join(stuff[3:5]----》'#')

2.将这两种方式翻译为自然语言。
' ' .join(stuff)  			用 ' ' 连接(join) stuff		
join(stuff-----》' ' )	    为 ' '和 stuff 调用 join 函数

3.上网阅读一些关于“面向对象编程(Object Oriented Programming)”的资料。
晕了吧？嗯，我以前也是。别担心。你将从这本书学到足够用的关于面向对象编程的基础知识，而以后你还可以慢慢学到更多。

4.查一下 Python中的 “class” 是什么东西。不要阅读关于其他语言的 “class” 的用法，这会让你更糊涂。

5.如果你不知道我讲的是些什么东西，别担心。
程序员为了显得自己聪明，于是就发明了 Opject Oriented Programming，简称为 OOP，然后他们就开始滥用这个东西了。
如果你觉得这东西太难，你可以开始学一下 “函数编程(functional programming)”。

6.找出10种可以放在列表中的例子，并用它们写一些脚本。
"""