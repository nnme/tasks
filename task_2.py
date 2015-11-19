# _*_ coding: utf-8 _*_
"""Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона."""
#make function for fibinacci 
def fib(n):
    result = []
    a, b, = 1, 0
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

#make list fib 
LIST = fib(4000000)

#make list /2
LIST2 = LIST[::3]

print 'spisok vseh chetnih chisel po fib', LIST2

#make sum from LIST2
summa = 0

for i in LIST2:
    summa = i+summa

print 'otvet na zadanie - ',  summa
