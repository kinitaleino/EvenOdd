a = [int(i) for i in input().split()] #принимает пользовательский ввод набором чисел в одной строке
b = []  #пустые массивы для четных и нечетных чисел
c = []
for i in a: #цикл для каждого значения списка а опеределяет четность 
    if i%2 == 0:
        b +=[i]
    else:
        c +=[i] 
b1 = sorted(b) #сортировка списков в порядке возрастания 
xc1 = sorted(c)
c1 = xc1[::-1] #создание списка перевернутого относительно xc1
print(b1)
print(c1)
result = b1 + c1 
print(result)