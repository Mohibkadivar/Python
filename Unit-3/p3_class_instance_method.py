class MyClass:
    count = 0

    def __init__(self, name):
        self.name = name
        MyClass.count += 1

    def instance_method(self):
        print(f"Instance method called. Name: {self.name}")

    @classmethod
    def class_method(cls):
        print(f"Class method called. Total objects created: {cls.count}")

    @staticmethod
    def static_method():
        print("Static method called. No access to class or instance.")

obj1 = MyClass("Alice")
obj2 = MyClass("Bob")

obj1.instance_method()
obj2.instance_method()
MyClass.class_method()
MyClass.static_method()
