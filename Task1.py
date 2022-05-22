#Сформировать список из N членов последовательности.

print('Введите количество элементов в списке:')
count = int(input())
print('Введите число с которого будет начинаться список:')
numb = float(input())
mas = []
for i in range(count):
    mas.append(round(numb, 2))
    numb *= -1.45
print(mas)
