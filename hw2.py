# Задание 2
# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Объяснить полученный результат.

a = 5
print(a, "=", bin(a)[2:])
b = 6
print(b, "=", bin(b)[2:])

print(a, "&", b, "=", a & b, "->", bin(a & b)[2:])
print(a, "|", b, "=", a | b, "->", bin(a | b)[2:])
print("~", a, "=", ~a, "->", bin(~a))
print(a, "<<", 2, "=", a << 2, "->", bin(a << 2)[2:])
print(a, ">>", 2, "=", a >> 2, "->", bin(a >> 2)[2:])