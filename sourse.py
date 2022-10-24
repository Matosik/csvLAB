import csv
import os
import shutil
from pathlib import Path
import random
import sys


def make_csv(name_csv: str) -> None:
    """Функция создает файл разрешения csv

    Args:
        name_csv (str): _название файла, который нужно создать_
    """
    with open(f"{name_csv}.csv", "w+", encoding="UTF-8", newline="") as file:
        csv_file = csv.writer(file, delimiter=";")
        csv_file.writerow(["Absolute path", "Relative path", "Class"])


def make_file_abstract(name_class: str, full_way: str, file_name: str) -> None:
    """Функция заполняет csv файл. В первый столбец полный путь файлов, второй столбец - путь

    Args:
        name_class (str)): _Название класса_
        full_way (str): _Полный путь к файлу_
        file_name (str): _имя файла разрешения csv_
    """
    full_way += name_class
    way = f"dataset/{name_class}/"
    folder = Path(full_way)
    if folder.is_dir():
        counter_files = len([1 for file in folder.iterdir()])  #
    with open(f"{file_name}.csv", "a", encoding="UTF-8", newline="") as file:
        csv_file = csv.writer(file, delimiter=";")
        for i in range(counter_files):
            csv_file.writerow([full_way + f"/{i}.jpg", way + f"{i}.jpg", name_class])


def porting(name_abstract: str, new_csv: str) -> None:
    """Функция импортируют файлы из собранного датасета в новый датасет. Файлы именуются по принципу "класс_Имяфайла.jpg"
        так же функция создает новый csv файл для нового датасета

    Args:
        name_abstract (str): имя csv из которого берем путь, имя и класс
        new_csv (str): имя csv файла в которой импортируем новый путь, имя и класс
    """
    try:
        os.mkdir("dataset")
    except:
        print("====ФАЙЛ ИМЕЕТСЯ====")
    with open(f"{name_abstract}.csv", newline="") as file:
        read = csv.DictReader(file, delimiter=";")
        with open(f"{new_csv}.csv", "a", encoding="UTF-8", newline="") as file1:
            csv_file = csv.writer(file1, delimiter=";")
            for row in read:
                FROM = row["Absolute path"]
                a = FROM.split("/")
                TO = f"dataset/{a[-2]}_{a[-1]}"
                shutil.copyfile(FROM, TO)
                name_class = row["Class"]

                fullWay = os.getcwd() + f"\dataset\{a[-2]}_{a[-1]}"
                Way = f"dataset\{a[-2]}_{a[-1]}"
                csv_file.writerow([fullWay, Way, name_class])


def random_name(file_abstract: str, new_abstract: str) -> None:  # 3 путкт
    """Функция импортируют файлы из собранного датасета в новый датасет с рандомным названием файла
        так же создается новый csv для навого датасета  для того чтобы осталась возможность определить принадлежность экземпляра к классу
    Args:
        file_abstract (str): имя csv из которого берем путь, имя и класс
        new_abstract (str):  имя csv файла в которой импортируем новый путь, имя и класс
    """
    b = []
    for i in range(0, 10001):
        b.append(i)
    c = random.sample(b, 2200)
    i = 0
    try:
        os.mkdir("dataset_random")
    except:
        print("====ФАЙЛ ИМЕЕТСЯ====")
    with open(f"{file_abstract}.csv", newline="") as file:
        read = csv.DictReader(file, delimiter=";")
        for row in read:
            FROM = row["Absolute path"]
            a = FROM.split("/")
            TO = f"dataset_random/{c[i]}.jpg"
            i += 1
            shutil.copyfile(FROM, TO)
            class_obj = row["Class"]
            with open(f"{new_abstract}.csv", "a", newline="") as file_new:
                csv_file = csv.writer(file_new, delimiter=";")
                slash1 = "\ "
                slash2 = "/"
                way = os.getcwd()
                counter = way.count(slash1[0])
                full_way = f"{way.replace(slash1[0],slash2,counter)}/{TO}"
                csv_file.writerow([full_way, TO, class_obj])


def next_way(read: csv.DictReader, mark: str) -> str:
    """Функция получающую на входе метку класса и возвращающую следующий экземпляр 

    Args:
        read (csv.DictReader): открытый csv файл
        mark (str): имя класса 

    Returns:
        str: путь к файлу или его отсутствие 
    """
    a = next(read)
    while True:
        try:
            if a["Class"] == mark:
                return a["Absolute path"]
            else:
                a = next(read)
        except:
            return "None"


class IteratorM:
    def __init__(self, file_name: str, class_name: str) -> None:
        self.limit = -1
        self.counter = -1
        self.file_name = file_name
        self.class_name = class_name
        self.rows = []
        with open(f"{file_name}.csv") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                if row[2] == class_name:
                    self.rows.append(row[0] + ";" + row[2])
                    self.limit += 1

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.counter < self.limit:
            self.counter += 1
            return self.rows[self.counter]
        else:
            print("None")
            raise StopIteration


full_way = "C:/Users/79093/Desktop/Application progra/parser/dataset/"
class_dog = "DogsIT"
class_cat = "CatIT"
# ========================= 1 пункт===========================
file_abstract = input("Введите название файла-анотация для 1 пункта : ")
make_csv(file_abstract)
make_file_abstract(class_dog, full_way, file_abstract)
make_file_abstract(class_cat, full_way, file_abstract)
# ========================= 2 пункт===========================
second_abstract = input("Введите название файла-анотация для 2 пункта : ")
make_csv(second_abstract)
porting(file_abstract, second_abstract)
# ========================= 3 пункт===========================
random_abstract = input("Введите название файла- анотация для 3 пункта: ")
make_csv(random_abstract)
random_name(file_abstract, random_abstract)
# ========================= 4 пункт===========================
name_file1 = input("Введите имя файла из которого хотите получить путь: ")
file = open(f"{name_file1}.csv")
reader = csv.DictReader(file, delimiter=";")
counter_dog = int(input("Введите сколько хотите вывести путей для собак: "))
for i in range(counter_dog):
    print(next_way(reader, class_dog))

file.close()
file = open(f"{name_file1}.csv")
reader = csv.DictReader(file, delimiter=";")
counter_cat = int(input("Введите сколько хотите вывести путей для кошек: "))
for i in range(counter_cat):
    print(next_way(reader, class_cat))

file.close()
# ========================= 5 пункт===========================
name_csv = input("Введите имя файла из которого хотите получить путь/пути: ")
counter_dog = int(input("Введите сколько хотите вывести путей для собак: "))
li_dog = IteratorM(name_csv, class_dog)
for i in range(counter_dog):
    print(next(li_dog))

counter_cat = int(input("Введите сколько хотите вывести путей для кошек: "))
li_cat = IteratorM(name_csv, class_cat)
for i in range(counter_cat):
    print(next(li_cat))
