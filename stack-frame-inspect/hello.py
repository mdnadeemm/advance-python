import inspect
def hello():
    x = 10
    frame = inspect.currentframe()  #stack frame
    print(frame.f_globals)  #global variables
    #print(frame.f_locals)  #local variables
    #print(frame)
    print(frame.f_code)  #current code object

hello()
