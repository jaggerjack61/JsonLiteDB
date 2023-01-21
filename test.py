def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))

def GET(route):
    def decorator(func):
        def wrapper():
            print('the route is '+str(route))
            func()
        return wrapper
    return decorator

@GET('api/products')
def showProducts():
    print('products here')

foo('test')
showProducts()