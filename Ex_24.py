Задача 24
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint

numBushes = int(input("Введите число кустов:  "))
berriesOnBushes_1 = [randint(1, 10) for i in range(numBushes)]
berriesOnBushes_2 = [randint(0,0) for i in range(numBushes)]
print (berriesOnBushes_1)
print (berriesOnBushes_2)

k = 2
for i in range(len(berriesOnBushes_1)):
    new_pos = ( i + k) % len(berriesOnBushes_1)
    berriesOnBushes_2[new_pos] = berriesOnBushes_1[i]
print (berriesOnBushes_2)

summaBerries_1 = 0
for i in range(numBushes-1):
    summaBerries_1 = berriesOnBushes_1[i-1] + berriesOnBushes_1[i] + berriesOnBushes_1[i+1]
print (summaBerries_1)

summaBerries_2 = 0
for i in range(numBushes -1):

    summaBerries_2 = berriesOnBushes_2[i-1] + berriesOnBushes_2[i] + berriesOnBushes_2[i+1]
print (summaBerries_2)

if summaBerries_1 > summaBerries_2:
    print(summaBerries_1)
else:
    print(bsummaBerries_2)