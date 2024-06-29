import os
# import glob

fi = os.path.join(os.getcwd(), '../file_list/recipe.txt')  # полный путь к файлу
# Задание №1


def get_cook_book():  # функция для получения словаря
    with open(fi, 'r', encoding='utf-8') as fl:  # открываем файл
        cook_book = {}  # создаем словарь
        for dish in fl:  # перебираем строки
            try:
                quantity_ingredient = int(fl.readline())  # считываем количество ингредиентов
                ingredients = []  # создаем список ингредиентов
                for ingredient in range(quantity_ingredient):  # перебираем ингредиенты
                    name, quantity, measure = fl.readline().strip().split(
                        '|'
                    )  # считываем ингредиенты
                    ingredients.append({
                        'ingredient_name': name,
                        'quantity': quantity,
                        'measure': measure
                    })  # добавляем ингредиенты в список
                fl.readline()  # считываем пустую строку
                cook_book[
                    dish.strip()] = ingredients  # добавляем ингредиенты в словарь
            except ValueError:
                print(f"Блюдо отсутствует в меню: {dish.strip()}")
        return cook_book  # возвращаем словарь


print(get_cook_book())
print()
# Задание №2


def get_shop_list_by_dishes(dishes: list, person_count: int):  # функция для получения списка покупок
    res = {}  # создаем словарь
    for dish in dishes:  # перебираем блюда
        if dish in get_cook_book().keys():  # если блюдо есть в книге рецептов
            for i in get_cook_book()[dish]:  # перебираем ингредиенты
                if i['ingredient_name'] not in res:  # если ингредиента нет в словаре
                    res[i['ingredient_name']] = {'measure': i['measure'],
                                                 'quantity': int(
                                                     i['quantity']) * person_count}  # добавляем ингредиент в словарь
                else:
                    res[i['ingredient_name']]['quantity'] += int(
                        i['quantity']) * person_count  # добавляем ингредиент в словарь
        else:
            return f'Блюдо "{dish}" отсутствует в кулинарной книге!'  # если блюда нет в кулинарной книге
    return res


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print()

# Задание №3

location = os.path.join(os.getcwd())  # получить текущее местоположение рабочего каталога здесь
counter = 0  # вести подсчет всех найденных файлов
txt_files = []  # список для хранения всех txt файлов, найденных в месте
file_list = []  # список отсортированных файлов по длине
rez = os.path.join(os.getcwd(), '../file_list/result.txt')  # путь к файлу для записи
for file in os.listdir(location):
    try:
        if file.endswith(".txt"):
            txt_files.append(str(file))
            counter = counter + 1
    except Exception as e:
        raise e

for file in txt_files:
    with open(file, encoding='utf-8') as f:  # Открываем файл
        text = f.readlines()  # Считываем файл
        file_list.append([file, len(text), text])  # Добавляем в список информацию о файле
    file_list.sort(key=lambda x: x[1])  # Сортируем по количеству строк
    with open(rez, 'w', encoding='utf-8') as result_file:  # Открываем файл для записи
        for file_data in file_list:  # Записываем в файл
            result_file.write((" ".join(file_data[2]))+'\n')
print('Файлы объединены!')  # Выводим сообщение об успешной записи
