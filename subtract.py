import time
from time_calculator import time_calculator

@time_calculator
def subtractFun(a, b):
    time.sleep(5)
    return a-b