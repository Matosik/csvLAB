import csv
import os
from pathlib import Path

def add_data(name_class,obj):
    full_way=f"C:/Users/79093/Desktop/Application progra/parser/dataset/{name_class}/"
    way=f"dataset/{name_class}/"
    with open("dataset_csv.csv", "a", encoding='UTF-8', newline='') as file:
        csv_file = csv.writer(file ,delimiter=';')
        csv_file.writerow(["Absolute path","Relative path","Class"])
    
        folder = Path(full_way)                                    #
        if folder.is_dir():                                        # считаем количество файлов 
            counter_files = len([1 for file in folder.iterdir()])  #
                                                                   #
        for i in range(counter_files):                             #заполняем файл эксайл 
            csv_file.writerow([full_way+f"{i}", way+f"{i}", obj])  #
    
class_dog="DogsIT"
class_cat="CatIT"
open("dataset_csv.csv", "w+", encoding='UTF-8', newline='')
add_data(class_dog,"dog")
add_data(class_cat,"cat")
