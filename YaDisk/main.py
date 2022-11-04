import requests
from my_toren import TOREN

URI = 'https://cloud-api.yandex.net/v1/disk/resources'
header = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}


class YaUpLoader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, ya_disk_path: str, file_path: str):
        params = {'path': ya_disk_path, 'overwrrite': 'true'}
        resp = requests.get(f'{URI}/upload', headers=header, params=params).json().get('href')
        with open(file_path, 'rb') as file_obj:
            respons = requests.put(resp, data=file_obj)
            if respons.status_code == 201:
                print('успешно')
            else:
                print(respons.status_code)


if __name__ == '__main__':
    path_to_file = 'D:\Рабочая\ЯндексДиск'
    token = TOKEN
    uploader = YaUpLoader(TOKEN)
    result = uploader.upload('Данные.txt', f'{path_to_file}\Данные.txt')