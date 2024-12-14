import os
import time

filepath = r'D:\Python\Module_7\main.py'

if os.path.isfile(filepath):
    filetime = os.path.getmtime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

    filesize = os.path.getsize(filepath)
    
    parent_dir = os.path.dirname(filepath)

    print(f'Обнаружен файл: {os.path.basename(filepath)}, Путь: {filepath}, Размер: {filesize} байт, '
          f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
