print("------------------------------------------------------------")
print("----------Решение Квадратных Уравнений by XayLoad-----------")
print("------------------------------------------------------------")

print("Задайте переменную - a")
a = float(input())
if a == 0:
    print("a не может быть = 0. Нажмите Enter что бы закончить.")
    exit(1)
print("Задайте переменную - b")
b = float(input())
print("Задайте переменную - c")
c = float(input())
print("a = ", a)
print("b =", b)
print("c = ", c)

disc = b ** 2 - 4 * a * c
disc2 = disc ** 0.5

print("Дискриминант D = ", disc)
print("Корень D = ", disc2)

x1 = -b + disc // 2 * a
x2 = -b - disc // 2 * a

x12 = -b + disc2 // 2 * a
x22 = -b - disc2 // 2 * a

if disc > 0:
    print("X1 = ", x1)
    print("X2 =", x2)
    print("X1 через корень = ", x12)
    print("X2 через корень=", x22)

elif disc == 0:
    x = -b / (2 * a)
    print("x = ", x)
else:
    print("Т.К. Д < 0 => Корней нет.")

print("Нажмите Enter что бы закончить программу")
input()
exit(2)
