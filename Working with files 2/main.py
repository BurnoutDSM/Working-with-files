import os

path = "files/"

def read_sort_book(path: str):
    files_list = os.listdir(path)
    files_dict = {}
    for file_name in files_list:
        if file_name.rfind('.txt', -4) >= 0:
            with open(os.path.join(path, file_name), 'r', encoding='utf-8') as file:
                files_dict[file_name] = file.readlines()

    with open('finish_book.txt', 'w', encoding='utf-8') as file:
        for file_name, rows in sorted(files_dict.items(), key=lambda item: len(item[1])):
            file.write(file_name + '\n')
            file.write(str(str(len(rows)) + '\n'))
            if '\n' not in rows[-1]:
                rows[-1] += '\n'
            file.write(''.join(rows))

read_sort_book(path)