# _*_ coding: utf-8 _*_
""""Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел - 23.

Найдите сумму всех чисел меньше 1000, кратных 3 или 5."""

# ===make list with natural number in diapason

# ===make list number /3
NUMB3 = [x for x in range(0,1000,3)]

# ===make list number /5
NUMB5 = [y for y in range(0,1000,5)]

R3 = 0 #var for "for"(3)
R5 = 0 #var for "for"(5)

# ===make list with natural number in diapason


# ===make sum in numb/3 and numb/5

# ===sum all number
for i in NUMB3:
    R3 = R3+i
# ===sum all number
for i in NUMB5:
    R5 = R5+i

# ===make sum in numb/3 and numb/5

# ===result
result = R3+R5

print 'summa all number/3 =', R3
print 'summa all number/5 =', R5
print 'pesult =', result
