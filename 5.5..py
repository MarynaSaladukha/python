f = open('text5.txt', 'w')
my_list = [1, 3, 5, 7, 9]
f.writelines(str(my_list))

i = 0
def listsum(my_list):
    my_sum = 0
    for el in my_list:
        my_sum = my_sum + el
    return my_sum


my_sum = listsum(my_list)
print(listsum(my_list))


