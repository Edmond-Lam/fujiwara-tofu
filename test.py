import time

def func_time(f):
	start = time.time()
	def inner(*arg):
		end = time.time()
		print "execution time: " + str(end - start)
		return f(*arg)
	return inner

def func_args( f ):
   def inner( *arg ):
       print f.func_name + ": " + str(arg)
       return f(*arg)
   return inner

@func_time
@func_args
def fibo(n):
    if n < 2:
       return n
    else:
       return fibo(n-1)+fibo(n-2)


print fibo(5)
