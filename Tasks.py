#Найти сумму чисел списка стоящих на нечетной позиции
#Пример:[1,2,3,4] -> 4 - подозреваю, что здесь ошибка, т.к нумерация списка начинается с 0 (четное число), тогда выходит что 2 + 4 = 6 стоящие соответсвенно на позиции 1 и 3

'''def create_array(array):
    abc = input('Введите число, если хотите закончить введите "end": ')
    while abc != 'end':
        array.append(int(abc))
        abc = input('Введите число, если хотите закончить введите "end": ')
        if abc == 'end':
            break

numbers = []
create_array(numbers)

count = 0
for i in range(len(numbers)):
    if i % 2 == 1:
        count += numbers[i]
print(count)'''

#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
#Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

'''def create_array(array):
    abc = input('Введите число, если хотите закончить введите "end": ')
    while abc != 'end':
        array.append(int(abc))
        abc = input('Введите число, если хотите закончить введите "end": ')
        if abc == 'end':
            break

def proizvedenie(array1, array2):
    if len(array1) % 2 == 0:
        n = len(array1) // 2
        for i in range(n):
            count = array1[i] * array1[len(array1)-1-i]
            array2.append(count)
    elif len(array1) % 2 == 1:
        n = len(array1) // 2
        for i in range(n):
            count = array1[i] * array1[len(array1)-1-i]
            array2.append(count)
        count = array1[n] ** 2
        array2.append(count)
    print(array2)
    

numbers = []
mas = []
create_array(numbers)
proizvedenie(numbers, mas)'''

#В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
#Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

'''def drob_array(arr):
    for i in range(len(arr)):
        ost = arr[i] % 1
        arr[i] = ost
    print(arr)

def ost(arr_65):
    max = 0
    for i in range(len(arr_65)):
       s = str(arr_65[i])
       n = abs(s.find('.') - len(s)) - 1
       if max < n:
           max = n
    return max
        
def sort(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    min = arr[0]
    for j in range(len(arr)):
        if 0 < arr[j] < min:
            min = arr[j]
    rez = max - min
    return rez

list = [1.1, 1.2, 3.1, 5, 10.01]
i = ost(list)
drob_array(list)
diff = sort(list)
print(f"{diff:.{i}f}")'''

#Написать программу преобразования десятичного числа в двоичное

'''numb = int(input('Введите число: '))
array = []
while numb > 1:
    a = numb % 2
    array.append(a)
    numb = numb // 2
array.append(1)
print(*array[::-1], sep='')'''