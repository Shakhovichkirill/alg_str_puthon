from alg_str_puthon.memory_def import total_size
print("Ноль в качестве знака операции завершит работу программы")
set_n = {'+', '-', '*', '/'}
tuple_n = ('+', '-', '*', '/')
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in set_n:             # or tuple_n
        x = float(input("x = "))
        y = float(input("y = "))
        if s == '+':
            print(f'{x + y:.2f}')
        elif s == '-':
            print(f'{x - y:.2f}')
        elif s == '*':
            print(f'{x * y:.2f}')
        elif s == '/':
            if y != 0:
                print(f'{x / y:.2f}')
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")

print(total_size(tuple_n, verbose=True))
print(total_size(set_n, verbose=True))

"""
280 - кортеж
80 <class 'tuple'> ('+', '-', '*', '/') 
50 <class 'str'> '+'
50 <class 'str'> '-'
50 <class 'str'> '*'
50 <class 'str'> '/'

424 - множество
224 <class 'set'> {'-', '*', '+', '/'}
50 <class 'str'> '-'
50 <class 'str'> '*'
50 <class 'str'> '+'
50 <class 'str'> '/'

Вывод:
С точки зрения затрачиваемой памяти лучше использовать кортеж, а с точки зрения поиска знака лучше использовать множество.
"""