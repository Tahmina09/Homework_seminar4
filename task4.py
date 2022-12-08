# 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

import random

k = int(input('Задайте натуральную степень: '))

with open('file_t4.txt', 'w') as data:
    i = k
    while i >= 0:
        num = random.randint(0, 10)   
        if num != 0:
            print('{} * (x ** {})'.format(num, i), end= ' + ', file= data)  
        if i == 0:
            print('{} = 0'.format(num), file= data)  
        i -= 1