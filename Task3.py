#Подсчитать сумму цифр в вещественном числе
numb = input()
count = 0
numb = numb.replace('.', '')
for i in numb:
    count += int(i)
print(count)