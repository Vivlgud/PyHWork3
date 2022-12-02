# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def dec_bin(num:int):
    """Перевод десятичного числа в двоичное"""
    if num==0:
        return list.reverse()
    num_dec = num % 2
    list.append(num_dec)
    dec_bin(num // 2)

while True:
    flag='q'
    number=input("Введите целое число или 'q' для выхода из программы: ")
    if number in flag:
        exit()
    else:
        number=int(number)
        list=[]
        dec_bin(number)
        print(list)

