#无尽模式训练你，检验所掌握的面向对象的单词和短语。
import random 
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"  #网页中全是单独成行的单词
WORDS = []

PHRASES = {  
	#创建一个叫%%%的类，并继承%%%。
	"class %%%(%%%):":
	  "Make a class named %%% that is-a %%%.",
	#类%%%有一个__init__方法，该方法有self和***两个参数。
	"class %%%(object):\n\t def __init__(self, ***)":
	  "class %%% has-a __init__ that takes self and *** parameters.",
	#类%%%有一个叫***的函数，该函数有self和@@@两个参数。
	"class %%%(object):\n\tdef ***(self, @@@)":
	  "class %%% has-a function named *** that takes self and @@@ parameters.",
	#给***赋值为类%%%的一个实例。
	"*** = %%%()":
	  "Set *** to an instance of class %%%.",
	#从***里调用***函数，传递的参数为self和@@@。
	"***.***(@@@)":
	  "From *** get the *** function, and call it with parameters self, @@@.",
	#从***里调用***属性，并将其设置为***。
	"***.*** = '***'":
	  "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
#由答题者选择是要根据描述编码还是根据代码描述。  
  

#sys.argv为从命令行接收的参数，第一个参数默认为文件名。
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True #True表示先打印value，按下任意键后再打印key
else:
	PHRASE_FIRST = False 
	
	
# load up the words from the website
#将词汇们载入到列表WORDS中
for word in urlopen(WORD_URL).readlines(): #一行一行从网页中读取数据
	WORDS.append(word.strip().decode("utf-8")) #删除每一行开始和结尾的空格，只留下单词并加入到words列表中
"""Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
str->bytes:encode编码，字符串通过编码成为字节码，
bytes->str:decode解码，字节码通过解码成为字符串。"""

#定义（覆盖描述和代码中预留位置的）函数，参数为片段、短语。  
#最后返回一个列表results  
#先将预留放置词汇的位置分类  
#参数为key或value，两个总是相对 	
def convert(snippet, phrase):
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***")) 
	"""random.sample(sequence, k) 从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列"""
	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		#参数的个数为1-3个随机。
		param_count = random.randint(1,3)
		#随机到几个参数就从WORDS中获取几个词
		param_names.append(', '.join(random.sample(WORDS, param_count)))
		
	#准备好要进行替换的PHRASES 
	for sentence in snippet, phrase:
		result = sentence[:]
		#result = [snippet, phrase]
#扯句闲话，作者为了片段和代码对应，替换词汇的顺序是固定的。。  
#用这种方法替换，描述与代码中词汇的顺序肯定是一样的。  
		#fake class names 类名 
		for word in class_names:
			result = result.replace("%%%", word, 1) #最后一位参数规定每次替换一个，保证%%%不重复。 
				
		#fake other names 对象、方法和其他 
		for word in other_names:
			result = result.replace("***", word, 1)
				
		#fake parameter lists  参数名  
		for word in param_names:
			result = result.replace("@@@", word, 1)
				
		results.append(result)
			
	return results
		
# keep going until they hit CTRL-D
#这里才是重点，是作者的编程逻辑。 
try:
	while True: #循环抽题
		snippets = list(PHRASES.keys()) #字典 keys() 方法：以列表返回一个字典所有的键。
		random.shuffle(snippets) #随机打乱顺序 
		
		for snippet in snippets: #抽题
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question
				
				print (question)
				
				input("> ")
				print ("ANSWER: %s\n\n" % answer)
except EOFError:
	print ("\nBye")
	
	
	