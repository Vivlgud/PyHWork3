# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# Fn = F(n+2)−F(n+1)



    
def fib(n:int):
    """Список чисел Фибоначчи для отрицательных и положительных индексов"""
    if n==0:
        return 0
    if n in [1, 2]:
        return 1
    if n<0:
        return fib(n+2) - fib(n+1)
    else:
        return fib(n-1) + fib(n-2)


while True:
    flag='q'
    number=input("Введите целое число или 'q' для выхода из программы: ")
    if number in flag:
        exit()
    else:
        number=int(number)
        list=[]
        for i in range(-number, number+1):
            list.append(fib(i))
        print(list)
        

