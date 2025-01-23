import time
def time_calculator(fun):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fun(*args, **kwargs)
        end_time = time.time()
        print(f"The execuation time of {fun.__name__} is {end_time-start_time} second.")
        return result
    return wrapper