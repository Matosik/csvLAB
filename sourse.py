from asyncio import shield
import csv
import os
import shutil
from pathlib import Path
import random


def make_csv(name_csv):
    with open(f"{name_csv}.csv", "w+", encoding='UTF-8', newline='') as file:
        csv_file = csv.writer(file ,delimiter=';')
        csv_file.writerow(["Absolute path","Relative path","Class"])
        return csv_file

def make_file_abstract(name_class,full_way, file_name):#1 пункт
    
    full_way+=name_class
    way=f"dataset/{name_class}/"
    folder = Path(full_way)                                    #
    if folder.is_dir():                                        # считаем количество файлов 
        counter_files = len([1 for file in folder.iterdir()])  #
    with open(f"{file_name}.csv", "a", encoding='UTF-8', newline='') as file: 
        csv_file = csv.writer(file ,delimiter=';')                                                           
        for i in range(counter_files):                             #заполняем файл эксайл 
            csv_file.writerow([full_way+f"/{i}.jpg", way+f"{i}.jpg", name_class])  

def porting(  name_abstract):# 2 пункт 
    try:
        os.mkdir("dataset")
    except:
        print("====ФАЙЛ ИМЕЕТСЯ====")
    with open(f"{name_abstract}.csv",newline="") as file:
        read= csv.DictReader(file,  delimiter=';')

        for row in read:
            FROM=row["Absolute path"]
            a=FROM.split("/")
            TO=f"dataset/{a[-2]}_{a[-1]}"
            shutil.copyfile(FROM,TO)

        
def random_name(file_abstract, new_abstract):# 3 путкт 
    b=[]
    for i in range(0,10001):
        b.append(i)
    c=random.sample(b,2200)
    i=0
    try:
        os.mkdir("dataset_random")
    except:
        print("====ФАЙЛ ИМЕЕТСЯ====")
    with open(f"{file_abstract}.csv",newline="") as file:
        read= csv.DictReader(file,  delimiter=';')
        for row in read:
            FROM=row["Absolute path"]
            a=FROM.split("/")
            TO=f"dataset_random/{c[i]}.jpg"
            i+=1
            shutil.copyfile(FROM,TO)
            class_obj=row["Class"]
            with open(f"{new_abstract}.csv","a" ,newline="") as file_new:
                csv_file = csv.writer(file_new ,delimiter=';') 
                slash1="\ "
                slash2="/"
                way=os.getcwd()
                counter=way.count(slash1[0])
                full_way=f"{way.replace(slash1[0],slash2,counter)}/{TO}"
                csv_file.writerow([full_way,TO,class_obj])
    
full_way="C:/Users/79093/Desktop/Application progra/parser/dataset/"
class_dog="DogsIT" #папка где собаки 
class_cat="CatIT"  #папка где кошки
#========================= 1 пункт===========================
file_abstract=input("Введите название файла-анотация для 1 пункта : ") 
make_csv(file_abstract)
make_file_abstract(class_dog, full_way,file_abstract)
make_file_abstract(class_cat, full_way,file_abstract)

#========================= 2 пункт===========================
porting(file_abstract)

#========================= 3 пункт===========================
random_abstract=input("Введите название файла- анотация для 3 пункта: ")
make_csv(random_abstract)
random_name(file_abstract,random_abstract)

#========================= 4 пункт===========================
