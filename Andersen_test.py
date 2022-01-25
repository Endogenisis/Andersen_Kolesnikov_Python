print("Введите число:")
n = int(input())
if n > 7:
    print("Привет!")

print("Введите имя:")
name = input()
if name == "Вячеслав":
    print("Привет, " + name)
else: print("Нет такого имени.")

print("Введите числа через пробел:")
l = [int(i) for i in input().split()]
for i in range(len(l)-1, -1, -1):
    if l[i] % 3 != 0 or l[i] == 0:
        l.remove(l[i])
print(l)
