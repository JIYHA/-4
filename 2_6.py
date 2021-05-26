import datetime
import os
import shutil
import sys

def main_func(path = os.getcwd(), days=2, size=4096):
    if os.path.isdir(path):
        files = os.listdir(path)
        for file in files:
            if os.path.isdir(path+"/"+"Archive")  and datetime.datetime.today().date() - datetime.datetime.fromtimestamp(os.path.getmtime(path+"/"+file)).date() > datetime.timedelta(days):
                shutil.copyfile(path +"/"+ file, path +"/" + "Archive/"+file)
            if not os.path.isdir(path+"/"+"Archive")  and datetime.datetime.today().date() - datetime.datetime.fromtimestamp(os.path.getmtime(path+"/"+file)).date() > datetime.timedelta(days):
                os.mkdir(path+"/"+"Archive")
                shutil.copyfile(path+"/"+file, path+"/"+"Archive/"+file)
            if os.path.isdir(path + "/" + "Small") and os.path.getsize(path + "/" + file) < size:
                shutil.copyfile(path + "/" + file, path + "/" + "Small/"+file)
            if not os.path.isdir(path+"/"+"Small") and os.path.getsize(path+"/"+file) < size:
                os.mkdir(path + "/" + "Small")
                shutil.copyfile(path + "/" + file, path + "/" + "Small/"+file)
        print("Хозяин, я закончил!")
    else:
        print("Заданной директории не существует")

if __name__ == '__main__': #точка входа в программe
    if sys.argv[1] =="--source" and sys.argv[3]=="--days" and sys.argv[5]=="--size" and str.isdigit(sys.argv[4]) and str.isdigit(sys.argv[6]):
       main_func(str(sys.argv[2]),int(sys.argv[4]),int(sys.argv[6]))
    else:
        print('Ошибка передачи параметров в скрипт. \nПример правильного ввода:python 6.py --source "C:/Users/Admin/PycharmProjects/Lab2/Task3" --days 2 --size 4096')
        