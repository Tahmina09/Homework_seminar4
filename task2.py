# 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите натуральное число N: '))

def prime_numbers(n):
    res_list = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            res_list.append(i)
    
    return res_list

print(prime_numbers(N))