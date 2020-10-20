spisok = [2.1, "Homework", "!", 12.5, None]
print(type(spisok))
#print(type(list[0]))
#print(type(list[1]))
#print(type(list[2]))
#print(type(list[3]))
#print(type(list[4]))
print(len(spisok))
i = 0
while i < len(spisok):
    val = type(spisok[i])
    i += 1
    print(val)

