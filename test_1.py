import pytest
import requests
from APIRoutes import APIRoutes
import pprint

#1
random_dog_image_response = requests.get(APIRoutes.get_random_dog_image())
random_dog_image = random_dog_image_response.json()['message']
def test_random_dog_image():
    assert random_dog_image.startswith('https://')

#2
shiba_images_response = requests.get(APIRoutes.get_dog_images_by_breed('shiba'))
shiba_images = shiba_images_response.json()['message']
pprint.pprint(shiba_images)

def test_shiba_image_count():
    assert len(shiba_images) > 0

@pytest.fixture
def dog_breeds():
    return ['bulldog', 'labrador', 'retriever', 'poodle']
#3
@pytest.mark.parametrize('breed', ['bulldog', 'labrador', 'poodle'])
def test_images_by_breed(breed):
    response = requests.get(APIRoutes.get_dog_images_by_breed(breed))
    assert response.status_code == 200, f"Не удалось получить {breed}"
    images = response.json()['message']
    assert len(images) > 0, f"Нет изображений {breed}"
    assert all(img.startswith('https://') for img in images[:5]), f"Неправильный путь {breed}"

#4 
@pytest.mark.parametrize('breed_key', ['bulldog', 'labrador', 'retriever', 'poodle'])
def test_breed_in_list(breed_key, dog_breeds):
    assert breed_key in dog_breeds, f"{breed_key} не найден"