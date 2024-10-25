
def greet(fx):
    def Mfx(*args,**kwargs):
        print("Hello good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return Mfx
@greet
def hello():
    print("hello All")
hello()

@greet
def add(a,b):
    print(a+b)

greet(add(2,4))

@greet
def multi(a,b):
    print(a*b)

greet(multi(2,4))