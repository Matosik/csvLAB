import csv
import os
import shutil
from pathlib import Path
import random
full_way="C:/Users/79093/Desktop/Application progra/parser/dataset/"
def get_nameclass():
    print("в разработке ")



def add_data(name_class,full_way):#1 пункт 
    full_way+=name_class
    way=f"dataset/{name_class}/"
    with open("dataset_csv.csv", "a", encoding='UTF-8', newline='') as file:
        csv_file = csv.writer(file ,delimiter=';')
        csv_file.writerow(["Absolute path","Relative path","Class"])
    
        folder = Path(full_way)                                    #
        if folder.is_dir():                                        # считаем количество файлов 
            counter_files = len([1 for file in folder.iterdir()])  #
                                                                   
        for i in range(counter_files):                             #заполняем файл эксайл 
            csv_file.writerow([full_way+f"{i}", way+f"{i}", name_class])  

def pack(class_obj):# 2 пункт 
    way=f"C:/Users/79093/Desktop/Application progra/parser/dataset/{class_obj}"
    try:
        os.mkdir("dataset")
    except:
        print("====ФАЙЛ ИМЕЕТСЯ====")
    for i in range(1100):
        shutil.copyfile(way+f"/{i}.jpg",way_to+f"/{class_obj}_{i}.jpg")




def add_random(full_name, obj,id):# 3 путкт 
    with open("dataset_random", "a", encoding="utf-8",newline="") as file:
        csv_file=csv.writer(file, delimiter=";")
        csv_file.writerow(["Absolute path", "Relative path", "Class", "Name_file"])
    
        
def random_name(cat,dog, way_from, way_to):# 3 путкт 
    a=[]
    for i in range(0,10001):
        a.append(i)
    try:
        os.mkdir("dataset_random")
    except:
        print("====ФАЙЛ ИМЕЕТСЯ====")
    for i in range(1100):
        c=random.sample(a,1100)
        shutil.copyfile(way_from+f"/{dog}_{i}.jpg",way_to+f"/{c[i]}.jpg")
    for i in range(1100):
        c=random.sample(a,1100)
        shutil.copyfile(way_from+f"/{cat}_{i}.jpg",way_to+f"/{c[i]}.jpg")


    
class_dog="DogsIT" #папка где собаки 
class_cat="CatIT"  #папка где кошки 
open("dataset_csv.csv", "w+", encoding='UTF-8', newline='')

add_data(class_dog, full_way)
add_data(class_cat, full_way)

way_from="C:/Users/79093/Desktop/Application progra/csv/dataset"
way_to="C:/Users/79093/Desktop/Application progra/csv/dataset_random"

pack(class_dog,way_from, way_to)
pack(class_cat, way_from,way_to)
random_name(class_cat,class_dog)