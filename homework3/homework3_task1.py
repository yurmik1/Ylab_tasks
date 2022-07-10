
if __name__ == '__main__':

    d = dict()


    def func_decorator(func):
        def wrapper(number):
            if not d.get(number):
                d[number] = func(number)
            return d[number]
        return wrapper


    @func_decorator
    def multiplier(number: int):
        return number * 2


