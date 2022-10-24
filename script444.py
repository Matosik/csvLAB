import csv

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

class_dog = "DogsIT"
class_cat = "CatIT"
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