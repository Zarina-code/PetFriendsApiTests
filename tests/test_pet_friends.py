import os
from unittest import result

from Tools.scripts.patchcheck import status

from api import PetFriends
from settings import valid_email, valid_password, invalid_email


pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """Получаем ключ API, который возвращает статус 200 и в результате содержит слово 'key'"""

    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_for_invalid_user(email=invalid_email, password=valid_password):
    """Проверяем что несуществующий пользователь не получает ключ API"""
    status = pf.get_api_key(email, password)
    assert status != 200

def test_get_all_pets_with_valid_key(filter=''):
    """Успешнеый запрос на получение всех животных"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_get_all_pets_with_invalid_key(filter=''):
    """Негативный тест на запрос на получение всех питомцев с неверным email"""
    _, auth_key = pf.get_api_key(invalid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200

def test_post_api_pets_with_valid_data(name='Maya', animal_type='bird', age='5', pet_photo='images/Maya.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_info_about_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_delete_api_pets_with_valid_key(pet_id='542c477f-03af-47bc-970e-59ed85396b54'):
    """Удаляем питомца по id"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    """Запрашиваем ключ API"""

    _, all_pets = pf.get_list_of_pets(auth_key, "")
    """Запрашиваем список всех питомцев"""

    pet_id = all_pets['pets'][0]['id']
    status, _ = pf.delete_info_about_pet(auth_key, pet_id)
    """Удаляем питомца по id"""
    assert status == 200
    assert pet_id not in all_pets.values()

def test_update_api_pets_with_valid_key(pet_id='542c477f-03af-47bc-970e-59ed85396b54'):
   """Успешное обновление информации о питомце"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    """Запрашиваем ключ API"""

    _, all_pets = pf.get_list_of_pets(auth_key, "")
    """Запрашиваем список всех питомцев"""

    assert status == 200
    assert result['name'] == name

def test_update_api_pets_with_invalid_key(pet_id=''):
    """Обновление информации о питомце с неверным email"""
    _, auth_key = pf.get_api_key(invalid_email, valid_password)
    _, all_pets = pf.get_list_of_pets(auth_key, "")
    assert status != 200

def test_update_pet_photo_with_valid_key(pet_photo='download.jpg'):
   """Успешное обновление фото питомца"""

   pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
   _, auth_key = pf.get_api_key(valid_email,valid_password)
   _, auth_key = pf.get_list_of_pets(auth_key, "")
   assert status == 200
   assert result['pet_photo'] is not ''

def test_update_pet_photo_with_invalid_key(pet_photo='download.jpg'):
    """обновление фото питомца с неверным email"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(invalid_email, valid_password)
    _, auth_key = pf.get_list_of_pets(auth_key, "")
    assert status != 200
