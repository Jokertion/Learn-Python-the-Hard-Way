from sys import argv  			    	            #引用模块

script, filename = argv			    	            #获取文件名

txt = open(filename)			      	            #打开文件

print ("Here's your file %r:" %filename)      #显示文件名
print (txt.read())		   		                  #读取文件 
txt.close()
print ("Type the filename again:")            #提示再次输入文件名
file_again = input(">")		      	            #输入文件名

txt_again = open(file_again)	  	            #再次打开文件

print (txt_again.read())	    		            #读取文件
  
txt.close()
