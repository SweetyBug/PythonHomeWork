#Написать программу получающую набор произведений чисел от 1 до N.
numb = int(input())
count = 1
for i in range(1, numb+1):
    count *= i
    print(count)
