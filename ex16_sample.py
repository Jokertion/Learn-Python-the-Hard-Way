from sys import argv  				#引用模块

script, filename = argv				#获取文件名

txt = open(filename)				#打开文件

print ("Here's your file %r:" %filename)  #显示文件名
print (txt.read())		   		    #读取文件 
txt.close()

