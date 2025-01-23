import time
from time_calculator import time_calculator
from subtract import subtractFun
@time_calculator
def add(a, b):
    time.sleep(5)
    return a+b



if __name__ == "__main__":
    print(add(5,3))
    print(subtractFun(5,3))
