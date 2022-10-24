import csv
import os
import random
import shutil

def make_csv(name_csv: str) -> None:
    """Функция создает файл разрешения csv

    Args:
        name_csv (str): _название файла, который нужно создать_
    """
    with open(f"{name_csv}.csv", "w+", encoding="UTF-8", newline="") as file:
        csv_file = csv.writer(file, delimiter=";")
        csv_file.writerow(["Absolute path", "Relative path", "Class"])

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


file_abstract = input("Введите название файла-анотация из которого извлечем информацию для нового csv файла: ")
random_abstract = input("Введите название файла- анотация для 3 пункта: ")
make_csv(random_abstract)
random_name(file_abstract, random_abstract)