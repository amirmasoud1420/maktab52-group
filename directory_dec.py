import os
from typing import *


def convert_unit( unit: Literal['B', 'KB', 'MB', 'GB']):
    def wapper(func):
        def innier(*args, **kwargs):
            if unit == 'B':
                return func(*args)
            elif unit == 'KB':
                return (func(*args) / 1024)
            elif unit == 'MB':
                return (func(*args) / (1024 ** 2))
            elif unit == 'GB':
                return (func(*args) / (1024 ** 3))
            else:
                raise Exception("Invalid unit")
        return innier

    return wapper

@convert_unit('KB')
def get_size(folder_path):
    sum_ = 0
    list_of_files = os.listdir(folder_path)
    for i in list_of_files:
        file_name = folder_path + i
        if os.path.isfile(file_name):
            sum_ += os.path.getsize(file_name)
        else:
            sum_ += get_size(file_name + "/")
    return sum_


# folder_path = "G:\maktab52\projects/XO_Game" + "/"
# print(convert_unit('KB')(get_size)(folder_path))
# folder_path = os.getcwd()+"/"
folder_path = "./"
print(get_size(folder_path))
