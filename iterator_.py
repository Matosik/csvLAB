import csv

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

class_dog = "DogsIT"
class_cat = "CatIT"
name_csv = input("Введите имя файла из которого хотите получить путь/пути: ")
counter_dog = int(input("Введите сколько хотите вывести путей для собак: "))
li_dog = IteratorM(name_csv, class_dog)
for i in range(counter_dog):
    print(next(li_dog))

counter_cat = int(input("Введите сколько хотите вывести путей для кошек: "))
li_cat = IteratorM(name_csv, class_cat)
for i in range(counter_cat):
    print(next(li_cat))
