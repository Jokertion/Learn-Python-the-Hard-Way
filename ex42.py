## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## ?? Dog is-a Animal class 
class Dog(Animal):

	def __init__(self, name):
		## ?? Dog has-a name
		self.name = name

## ?? Cat is-a Animal class
class Cat(Animal):

	def __init__(self, name):
		## ?? Cat has-a name 
		self.name = name

## ??Person is-a object class
class Person(object):

	def __init__(self, name):
		## ?? Person has-a name  
		self.name = name

		## Person has-a pet of some kind
		self.pet = None  #默认属性

## ?? Employee is-a person class
class Employee(Person):

	def __init__(self, name, salary):
		## ?? Employee inherit Person hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ?? Employee has-a salary
		self.salary = salary

## ?? Fish is-a object class 
class Fish(object):
	pass

## ?? Salmon is-a Fish class 
class Salmon(Fish):
	pass

## ?? is-a Halibut is-a Fish class
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## ?? satan is-a  Cat
satan = Cat("Satan")

## ??Mary is-a person
mary = Person("Mary")

## ?? Mary has-a pet named satan
mary.pet = satan

## ?? frank is-a Employee
frank = Employee("Frank", 120000)

## ?? frank has-a dog named rover
frank.pet = rover

## ?? flipper is-a Fish
flipper = Fish()

## ?? is-a  crouse is-a Salmon Fish
crouse = Salmon()

## ?? harry is-a Halibut Fish 
harry = Halibut()