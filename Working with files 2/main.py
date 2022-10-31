# with open('file1.txt', 'r', encoding='utf-8') as f1:
#     f1_list = f1.readlines()
#
# with open('file2.txt', 'r', encoding='utf-8') as f2:
#     f2_list = f2.readlines()
#
# with open('file3.txt', 'r', encoding='utf-8') as f3:
#     f3_list = f3.readlines()
#
# if len(f1_list) < len(f2_list) and len(f1_list) < len(f3_list):
#     if len(f2_list) < len(f3_list):
#         book = f1_list, f2_list, f3_list
#     elif len(f2_list) > len(f3_list):
#         book = f1_list, f3_list, f2_list
#
# if len(f2_list) < len(f1_list) and len(f2_list) < len(f3_list):
#     if len(f1_list) < len(f3_list):
#         book = f2_list, f1_list, f3_list
#     elif len(f1_list) > len(f3_list):
#         book = f2_list, f3_list, f1_list
#
# if len(f3_list) < len(f1_list) and len(f3_list) < len(f2_list):
#     if len(f1_list) < len(f2_list):
#         book = f3_list, f1_list, f2_list
#     elif len(f1_list) > len(f2_list):
#         book = f3_list, f2_list, f1_list
# sort_book = []
# for item in book:
#     sort_book += item.strip()
# #print('\n'.join(b))
# print(*sort_book)
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