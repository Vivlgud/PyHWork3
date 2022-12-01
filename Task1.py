# 1- Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def summa_odd_index(new_list:list):
    '''Sum of list elements with odd indexes'''
    sum=0
    for i in range(1,len(new_list),2):
        sum+=new_list[i]
    return sum

new_list=(2,3,5,9,3)
result=summa_odd_index(new_list)
print(result)
