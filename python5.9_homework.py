import time

class Timer(object):
    def __init__(self, param=1):
        self.param = param
        # print("init", param)        
    def __call__(self, func):
        avg_time = 0
        for _ in range(self.param): 
            t0 = time.time()
            func()
            t1 = time.time()
            avg_time += (t1 - t0)            
        avg_time /= self.param
        print("Выполнение заняло %.5f секунд" % avg_time)     
    def __enter__(self):
        self.start_time = time.time()
        # print("enter")
    def __exit__(self, *args, **kwds):
        print("Выполнение заняло %.5f секунд" % (time.time() - self.start_time))
    
param = int(input("Введите число запусков для замера средней скорости"))

with Timer():
    for j in range(1000000):
        pass

@Timer(param)
def f():
    for j in range(1000000):
        pass
        