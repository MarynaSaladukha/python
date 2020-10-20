
user_text = input('Введите текст ')
print(user_text)
print(len(user_text))
last_letter = (len(user_text)-1)
print(last_letter)
i = 0 #будет соответствовать расположению пробела
start_cut = 0 #будет соответствовать началу среза
number_line = 0
while i <= last_letter:
    if user_text[i] == ' ' or i == last_letter:

        cut = user_text[start_cut:i + 1]

        lenght_word = len(cut)
        start_cut = i + 1
        number_line += 1
        if lenght_word <= 10:
            print(number_line, cut)
        else:
            print(number_line, cut[:10])

    i += 1





