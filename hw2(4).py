# Задание №2
import cProfile

# Алгоритм нахождения i - го по счету простого числ. Алгоритм решето Эратосфена
import cProfile
def erat(n, m):
    numbers = list(range(n + 1))
    numbers[1] = 0
    sieve = []
    for i in numbers:
        if i > 1:
            for j in range(i + i, len(numbers), i):
                numbers[j] = 0
        if i != 0:
            sieve.append(i)
    print(sieve[m])
#n - конечное число списка
#m - номер итого элемента

#timeit
# 100 loops, best of 5: 1.14 msec per loop - erat(100, 10)
# 1000 loops, best of 5: 965 usec per loop - erat(100, 10)

# 100 loops, best of 5: 1.09 msec per loop - erat(100, 10)
# 100 loops, best of 5: 2.96 msec per loop - erat(1000, 10)


#cProfile.run("erat(100, 10)")
   #       55 function calls in 0.000 seconds
   # Ordered by: standard name
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 test.py:3(erat)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #     25    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
   #     25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#cProfile.run("erat(10000000, 10)")
   #       1329163 function calls in 13.237 seconds
   # Ordered by: standard name
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.289    0.289   13.236   13.236 <string>:1(<module>)
   #      1   12.586   12.586   12.948   12.948 test.py:3(erat)
   #      1    0.000    0.000   13.237   13.237 {built-in method builtins.exec}
   # 664579    0.162    0.000    0.162    0.000 {built-in method builtins.len}
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
   # 664579    0.199    0.000    0.199    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Алгоритм нахождения i - го по счету простого числ.
def nat_num(a, b):
    sieve_oth = []
    for i in range(2, a + 1):
        for j in sieve_oth:
            if i % j == 0:
                break
        else:
            sieve_oth.append(i)
    print(sieve_oth[b])
#a - конечное число списка
#b - номер итого элемента

#timeit
# 100 loops, best of 5: 1.01 msec per loop - nat_num(100, 10)
# 100 loops, best of 5: 4.9 msec per loop - nat_num(1000, 10)

# 100 loops, best of 5: 768 usec per loop - nat_num(100, 10)
# 1000 loops, best of 5: 945 usec per loop - nat_num(100, 10)

#cProfile.run('nat_num(100, 10)')
# 30 function calls in 0.000 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 test.py:3(nat_num)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#cProfile.run('nat_num(100000, 10)')
# 9597 function calls in 11.016 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   11.016   11.016 <string>:1(<module>)
#         1   11.006   11.006   11.015   11.015 test.py:3(nat_num)
#         1    0.000    0.000   11.016   11.016 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#      9592    0.010    0.000    0.010    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

