import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"

    def get_api_key(self, email, password):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат
        с уникальным ключом пользователя"""

        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        """Метод делает запрос к сервера и возвращает статус запроса и результат
        со списком найденных питомцев. Фильтр может быть пустымм или 'my_pets' - список
        собственных питомцев"""
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_info_about_new_pet(self, auth_key, name, animal_type, age, pet_photo):
        """Метод отправляет на сервер данные о новом питомце и возвращает статус и результат
        с данными добавленного питомца"""

        data = MultipartEncoder(
            fields = {
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url+'api/pets', headers=headers, data=data)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_info_about_pet(self, auth_key, pet_id):
        """Метод отправляет запрос на сервер на удаление питомца по указанному ID"""

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key, pet_id, name, animal_type, age):
        """Метод отправляет запрос на сервер на обновление питомца по указанному ID"""

        data = MultipartEncoder(
            fields = {
                'name': name,
                'animal_type': animal_type,
                'age': age
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def update_pet_photo(self, auth_key, pet_id, pet_photo):
        """Метод отправляет запрос на обновление фото питомца по указанному ID"""

        data = MultipartEncoder(
            fields={'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}
        )
        headers = {'auth_key': auth_key['key'], 'Content_Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result