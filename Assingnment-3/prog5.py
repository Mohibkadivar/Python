def cal(a,b):
    def add():
        return a+b
    def multiply():
        return a*b
    print("addition",add())
    print("multiplication",multiply())
    
cal(5,3)