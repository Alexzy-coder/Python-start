# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('text2.txt', 'w', encoding='utf=8') as f:

    while True:
     text = input('Введите слово: ')
     if text == "":
         break
     else:
         f.write(text)
         f.write("\n")
     continue

with open('text2.txt', 'r', encoding='utf=8') as f:
     content = f.readlines()
     a = (len(content))  # считает количество строк

with open('text2.txt', 'r', encoding='utf=8') as f:
    for i, b in enumerate(content):
        words = len(b.split())
        print('Cтрока {} имеет количество слов {}'.format(i + 1, words))

print(f'Количество строк: {(a)}')






