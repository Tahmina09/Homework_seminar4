# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

oneList = [1, 1, 2, 3, 4, 4, 4]

def countSimilar(list1):
    counters = [0] * len(list1)
    for i in range(len(list1)):
        counters[list1[i]] += 1
        
    res_list = []
    for i in range(len(counters)):
        if counters[i] == 1:
            res_list.append(list1[i])
    print(res_list)
    
countSimilar(oneList)