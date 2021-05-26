'''
x = 'Hi'

def read_x():
	print(x)

read_x()
'''
'''
def ready_y():
	y = "Cachorra"
	print(y)

ready_y()
'''

def read_x_local_fail():
 if False:
	 x = 'Hey' # x appears in an assignment, therefore it's local
	 print(x) # will look for the _local_ z, which is not assigned, and will not be found
read_x_local_fail() 

#Local Variables
'''
def foo():
	a = 5
	print(a)

print(a)
'''
'''
def foo():
 if True:
   a = 5
   print(a) 
foo()
'''
'''
b = 3
def bar():
	if False:
		b = 5
		print(b)
bar()
'''