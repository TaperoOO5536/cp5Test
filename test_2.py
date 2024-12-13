import pytest
import requests
from APIRoutes import APIRoutes
import pprint
#1
brewery_city_1 = requests.get(APIRoutes.get_breweries_by_city('san_diego'))
pprint.pprint(brewery_city_1.json())
@pytest.mark.parametrize('param', [0, 1, 2])
def test_city(param):
    assert brewery_city_1.json()[param]['city'] == 'San Diego'

#2
brewery_city_3 = requests.get(APIRoutes.search_breweries('Gordon'))
pprint.pprint(brewery_city_3.json())

@pytest.mark.parametrize('param', [0, 1, 2])
def test_search(param):
    assert 'Gordon' in brewery_city_3.json()[param]['name'] or 'Gordon' in brewery_city_3.json()[param]['name']


#3
@pytest.mark.parametrize('city', ['san_diego', 'portland', 'denver'])
def test_breweries_by_city(city):
    response = requests.get(APIRoutes.get_breweries_by_city(city))
    breweries = response.json()
    assert len(breweries) > 0, f"Не найдено для города '{city}'"
    for brewery in breweries:
        assert brewery['city'].lower().replace(' ', '_') == city, f"Несоответствие города: {brewery['city']} != {city}"

#4
@pytest.mark.parametrize('query, expected_word', [
    ('gordon', 'Gordon'),
    ('mikkeller', 'Mikkeller'),
    ('brew', 'Brew')
])
def test_autocomplete_contains_query(query, expected_word):
    response = requests.get(APIRoutes.autocomplete_breweries(query))
    breweries = response.json()
    assert len(breweries) > 0, f"Не найдено '{query}'"
    for brewery in breweries:
        assert expected_word in brewery['name'], f"Отсутствует '{expected_word}' в названии, но есть {brewery['name']}"