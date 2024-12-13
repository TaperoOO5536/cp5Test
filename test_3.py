import pytest
import requests
from APIRoutes import APIRoutes

jsplace_info_data = requests.get(APIRoutes.get_posts_by_user(1)).json()
jsplace_title_data = requests.get(APIRoutes.get_posts_by_title('qui est esse')).json()
jsplace_body_data = requests.get(APIRoutes.get_posts_by_body('quia et suscipit')).json()
jsplace_id_data = requests.get(APIRoutes.get_post_by_id(1)).json()

#1
@pytest.mark.parametrize('param', [0, 1, 2])
def test_user_id(param):
    assert len(jsplace_info_data) > param, f"Пост с индексом {param} "
    assert jsplace_info_data[param]['userId'] == 1, f"Пост не совпадает с индексом {param}"

#2
@pytest.mark.parametrize('param', [0])
def test_title(param):
    assert len(jsplace_title_data) > param, f"Поиск по заголовку не дал результатов по индексу {param}"
    assert jsplace_title_data[param]['title'] == 'qui est esse', f"Несоответствие заголовка по индексу  {param}"    

#3
@pytest.mark.parametrize('param', [0, 1, 2])
def test_body_exclusion(param):
    if len(jsplace_body_data) <= param:
        pytest.skip(f"Нет поста по индексу {param}")
    assert 'quia et suscipit' not in jsplace_body_data[param]['body'], f"Неожиданный текст в body по индексу {param}"

#4
@pytest.mark.parametrize('param', [0])
def test_post_by_id(param):
    assert len(jsplace_id_data) > param, f"Сообщение с id 1 не найдено в индексе {param}"
    assert jsplace_id_data[param]['id'] == 1, f"Несоответствие идентификатора по индексу {param}"