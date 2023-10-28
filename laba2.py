# Чернова Александра Сергеевна 409837
import csv
from random import randint
import xml.dom.minidom as minidom

# Задание 1
with open("books.csv") as r_file:
    freader = csv.reader(r_file, delimiter=";")
    count = 0
    for row in freader:
        if len(list(row)[1]) > 30:
            count += 1
    print(count)

# Задание 2
print('Введите автора')
search = input().lower()
flag = 0
result = set()
with open("books.csv") as r_file:
    freader = csv.reader(r_file, delimiter=";")
    for row in freader:
        if list(row)[4].lower() == search or list(row)[3].lower() == search:
            date = int(list(row)[6][6:10])  # берем из даты только год
            if date >= 2016 and date <= 2018:  # условие варианта 7
                flag = 1
                result.add(row[1])
    if flag == 0:
        print('Ничего не найдено')
    else:
        for book in result:
            print(book)

# Задание 3
with open("books.csv") as r_file:
    freader = csv.reader(r_file, delimiter=";")
    flength = 0
    for row in freader:
        flength += 1  # считаем кол-во строчек
with open("books.csv") as r_file:
    freader = csv.reader(r_file, delimiter=";")
    random_list = [randint(1, flength) for i in range(20)]  # случайные 20 значений
    random_list.sort()
with open("books.csv") as r_file:
    in_use = list(csv.reader(r_file, delimiter=";"))
    with open('result.txt', 'w') as file:
        for i in random_list:
            file.write(str(i) + ' ' + in_use[i][3] + '. ' + in_use[i][1] + ' - ' + in_use[i][6] + '\n')
    file.close()

# Задание 4
xml_file = open('currency.xml', 'r', encoding='utf-8')
xml_data = xml_file.read()
dom = minidom.parseString(xml_data)
dom.normalize()
elements = dom.getElementsByTagName('Valute')
C_Code = []
for node in elements:
    nominal = int(node.getElementsByTagName('Nominal')[0].firstChild.data)
    if nominal == 10 or nominal == 100:
        char_code = node.getElementsByTagName('CharCode')[0].firstChild.data
        C_Code.append(char_code)
print(C_Code)

# Дополнительное задание
# Перечень всех тегов
with open("books.csv") as r_file:
    freader = csv.reader(r_file, delimiter=";")
    tags = set()  # множество тэгов
    for row in freader:
        if list(row)[0]=='ID':
            continue
        a = row[12].split('#')  # убираем хэштеги
        for tag in a:
            tags.add(tag.strip())  # добавляем в множество, убираем лишние пробелы

print('20 самых популярных книг:')
with open("books.csv") as r_file:
    freader = csv.reader(r_file, delimiter=";")
    info = []
    for row in freader:
        if [row[1], row[8]] not in info:  # проверяем, есть ли книга в списке
            info.append([row[1], row[8]])
    info = info[1:]
    info_sort = sorted(info, key=lambda x: int(x[1]), reverse=True)  # сортируем по значению "Кол-во выдач"
    for i in range(20):
        print(i+1, ')', info_sort[i][0])

