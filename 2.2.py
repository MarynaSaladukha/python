text = input("Введите слово ")
print(text)
a = list(text)
print(a[0])
i = 0
n = len(a)

while i < len(a) - 1:
    a[i], a[i + 1] = a[i + 1], a[i]
    i += 2
    print(a)

