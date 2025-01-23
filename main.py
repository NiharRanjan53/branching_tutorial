import time
def time_calculator(fun):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fun(*args, **kwargs)
        end_time = time.time()
        print(f"The execuation time of {fun.__name__} is {end_time-start_time} second.")
        return result
    return wrapper
@time_calculator
def add(a, b):
    time.sleep(5)
    return a+b

if __name__ == "__main__":
    print(add(5,3))
