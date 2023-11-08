# simple demo of how to use decorators. here we create a decorator function to see how long a function takes then pass this decorator to the functions this and that 

import time 
def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()-t1
        print(f'{func.__name__} ran in {t2} seconds')
    return wrapper

@tictoc        
def this():
    time.sleep(1)
    
@tictoc
def that():
    time.sleep(2)
    
this()
that()
print('Done')
