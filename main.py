import time
from time_calculator import time_calculator
from subtract import subtractFun
from newFeature import newFeature
@time_calculator
def add(a, b):
    time.sleep(5)
    return a+b

@time_calculator
def mul(a, b):
    time.sleep(2)
    return a*b

if __name__ == "__main__":
    print(add(5,3))
    print(subtractFun(5,3))
    print(mul(5, 3))
    newFeature()
