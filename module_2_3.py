# Домашняя работа по уроку "Стиль кода часть II. Цикл While."

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
z = 0

while z < len(my_list):

    if my_list[z] < 0:
        break

    if my_list[z] > 0:
        print(my_list[z])

    z = z + 1

    if my_list[z] == 0:
        continue