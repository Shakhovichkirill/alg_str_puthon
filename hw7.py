# Задание 7
# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

if A + B <= C or A + C <= B or B + C <= A:
    print("Треугольник не существует")
elif A != B and A != C and B != C:
    print("Разносторонний")
elif A == B == C:
    print("Равносторонний")
else:
    print("Равнобедренный")