import os
import time

# Путь к файлу
filepath = r'D:\Python\Module_7\main.py'

if os.path.isfile(filepath):
    # Получение времени последнего изменения файла
    filetime = os.path.getmtime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

    # Получение размера файла
    filesize = os.path.getsize(filepath)

    # Получение родительской директории
    parent_dir = os.path.dirname(filepath)

    # Вывод информации о файле
    print(f'Обнаружен файл: {os.path.basename(filepath)}, Путь: {filepath}, Размер: {filesize} байт, '
          f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
