#Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

def array(mass):
    mas = []
    for i in mass:
        if i not in mas:
            mas.append(i)
    return mas

def count_num(mas1, mas2):
    for i in mas1:
        count = 0
        for j in mas2:
            if i == j:
                count += 1
        print(f'Число {i} входит в список {count} раз')

def create_array(mass):
    a = input()
    while a != 'end':
        if a == 'end':
            break
        else:
            mass.append(int(a))
            a = input()

array1 = []
array2 = []

print('Введите значние в список 1, если захотите прервать напишите "end"')
create_array(array1)
print('Введите значние в список 2, если захотите прервать напишите "end"')
create_array(array2)

arr1 = array(array1)
arr2 = array(array2)

print('Вхождение первого списка во второй:')
count_num(arr1, array2)
print('Вхождение второго списка в первый:')
count_num(arr2, array1)
