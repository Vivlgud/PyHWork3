# 3-Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114

def diff_max_min(list_number:list):

    '''Разница между максимальным и минимальным значением дробной части элементов списка'''
    max_num=0
    min_num=min(list_number)

    for i in list_number:
        fractional_part=round(i-int(i),10)
        if fractional_part>max_num:
            max_num=fractional_part

        if fractional_part<min_num:
            min_num=fractional_part
       
    difference=round(max_num-min_num,10)  
    return difference          

list_number=(1.1,1.2,3.1,5.17,10.02)
# list_number=(4.07,5.1,8.2444,6.9814)
print(diff_max_min(list_number))











