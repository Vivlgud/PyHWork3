# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


def mult_pair(new_list:list):
    '''Произведение пар чисел списка'''
    
    list_result=[]
    num=0
    if len(new_list)%2==0:
        num=int(len(new_list)/2)
    else:
        num=int(len(new_list)/2+1)
        
    for i in range(num):
        list_result.append(new_list[i]*new_list[-(i+1)])
    return list_result

new_list=(2,3,4,5,6)

print(mult_pair(new_list))