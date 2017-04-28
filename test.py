def func_args( f ):
   def inner( *arg ):
       print f.func_name + ": " + str(arg)
       return f(*arg)
   return inner

#def foo( x, y, z ):
  
#  return [x+5,y+6,z]

#closure = wrapper(foo)
#print closure( 10000,6,"wow" ) #will run foo with the arguments -2, 3, 'hello' through wrapper


@func_args
def fibo(n):
    if n < 2:
       return n
    else:
       return fibo(n-1)+fibo(n-2)


print fibo(10)
