#创建州映射缩写
#create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan' : 'MI'
}

#创建州和州的一些城市
#creat a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#添加更多的城市
#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#打印一些城市
#print out some cities
print ('-' *10)
print ("NY State has: ", cities['NY'])
print ("OR State has: ", cities['OR'])

#打印一些州
#print some states
print ('-' *10)
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("Florida's abbreviation is: ", states['Florida'])

#以某州为参数，调用城市字典
#do it by using the state then cities dict
print ('-' *10)
print ("Michigan has: ", cities[states['Michigan']])
print ("Florida has: ", cities[states['Florida']])

#打印每个州的缩写
#print every state abbreviation
print ('-' *10)
for state, abbrev in states.items():
	print ("%s is abbreviated %s" % (state, abbrev)) 

	#打印每个城市所在的州
#print every city in state
print ('-' *10)
for abbrev, city in cities.items():
	print ("%s has the city %s" % (abbrev, city)) 

	#打印州-缩写-城市
#now do both at the same time 
print ('-' *10)
for state, abbrev in states.items():
	print ("%s state is abbreviated %s and has city %s" % (
		state, abbrev,cities[abbrev]))
#get（）获取字典中的元素:
#	返回指定键的值，如果值不在字典中返回默认值 None。None永远表示False		
print ('-' *10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

#None永远表示False
if not state:
	print ("Sorry, no Texas.")
	
#get a city with a default value
city = cities.get('TX', 'Dose Not Exist')
print ("The city for the state 'TX' is: %s" % city)

		




