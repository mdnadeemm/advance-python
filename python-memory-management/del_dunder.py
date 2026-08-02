class A:
    def __del__(self):
        print("Destroyed")


a = A()
del a
