class Outer:
    def __init__(self):
        self.outer_val = "I am Outer"
        self.inner = self.Inner()

    def display(self):
        print(self.outer_val)
        self.inner.display()

    class Inner:
        def __init__(self):
            self.inner_val = "I am Inner"

        def display(self):
            print(self.inner_val)

obj = Outer()
obj.display()
