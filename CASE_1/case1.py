import random #подключаем библиотеку рандом

N = int(input("введите колличество элементов")) #Запрашиваем у пользователя размер массива

#Создаем поле размером N
A = []*N

#Заполняем Массив элементами
for el in A:
    el = random.randint(-1000,1000)

#Находим максимум и минимум, создаем индексы максимума и минимума
maxi = max(A)
mini = min(A)
in_min = -2
in_max = -2

#Находим индексы максимума и минимума
for i in range(0,N):
    if A[i] == maxi:
        in_max = i
    if A[i] == mini:
        in_min = i

'''
Создаем переменную суммы и считаем сумму отрицательных
элементов по индексу и условию отрицательности
'''
sum = 0
if in_min < in_max:
    for i in range(in_min , in_max):
        if A[i] < 0:
            sum+= A[i]
else:
    for i in range(in_max , in_min):
        if A[i] < 0:
            sum+= A[i]

print(sum)
