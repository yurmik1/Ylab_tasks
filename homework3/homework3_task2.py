import time


if __name__ == '__main__':
    def df_decorator(call_count=1, start_sleep_time=2, factor=3, border_sleep_time=4):
        def func_decorator(func):
            def wrapper():
                print(f'Кол-во запусков = {call_count}')
                print('Начало работы')
                t = start_sleep_time * factor ** 0
                for i in range(1, call_count + 1):
                    time.sleep(t)
                    func_result = func()
                    if t % 10 == 1 and t % 100 != 11:
                        sec = "секунда"
                    elif t % 10 in [2, 3, 4] and t % 100 not in [12, 13, 14]:
                        sec = "секунды"
                    else:
                        sec = "секунд"
                    print(f'Запуск номер {i}. Ожидание: {t} {sec}. Результат декорируемой функций = {func_result}')
                    t = start_sleep_time * factor**(i) if start_sleep_time * factor**(i)\
                                                            < border_sleep_time else border_sleep_time
                print('Конец работы')
            return wrapper
        return func_decorator


    @df_decorator(call_count=5, start_sleep_time=1, factor=2, border_sleep_time=20)
    def function():
        return 'Функция выполнена'


    function()



