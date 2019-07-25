class Employee:
    classSpec = "it is a test class"
    def __init__(self, name, salary):  # 构造方法，传参，self自己，
        self.name = name

        self.salary = salary
    def hello(self):
        print(self.name)
