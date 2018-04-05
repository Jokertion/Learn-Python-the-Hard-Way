# -*- coding:utf-8 -*-
cars = 100  			 									    #车数
space_in_a_car =4.0     										#一辆的空座位数
drivers = 30													#司机数
passengers =90  											    #乘客数
cars_not_driven = cars - drivers 								#没被开的车数 = 车数-司机数
cars_driven = drivers     		 								#开的车数 = 司机数
carpool_capacity = cars_driven * space_in_a_car 			    #合计容量 = 开的车数*一辆的空座位数
average_passengers_per_car = passengers / cars_driven			#每辆车的平均乘客数 = 乘客数/开的车数


print ("There are", cars, "cars available.")						#这里有 车数  的车可用
print ("There are only", drivers, "drivers available.") 		    #这里只有 司机数 的司机可用
print ("There will be", cars_not_driven, "empty cars today.") 	#这里将要有 没被开的车数 的空车今天
print ("We can transport", carpool_capacity, "people today.")		#我们能运输 合计容量 的人今天 
print ("We have", passengers, "to carpool today.")				#我们有 乘客数 需要拉今天
print ("We need to put about", average_passengers_per_car, "in each car.")  #我们需要放置 每辆车的平均乘客数 在每辆车上
