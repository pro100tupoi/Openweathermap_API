import requests
# noinspection PyUnresolvedReferences
import pytest

API_key = '995fa1c5b9649503a3386aca1d3e32a4'
city_name = 'Saint Petersburg'

#http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_key}

# Формируем URL для запроса
Standard_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
Metric_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"
#Imperial_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=imperial"

# Отправляем GET-запрос
responseStandard = requests.get(Standard_url)
responseMetric = requests.get(Metric_url)
#responseImperial = requests.get(Imperial_url)

# Проверяем статус ответа
def test_url_api_get():
    assert responseStandard.status_code == 200,"URL для запроса температуры в кельвенах не прошел"
    assert responseMetric.status_code == 200,"URL для запроса температуры в цельсиях не прошел"

data_Metric = responseMetric.json()
data_Standard = responseStandard.json()

# Извлекаем данные
temperature_celsius = data_Metric["main"]["temp"]
temperature_fromkelvin = data_Standard["main"]["temp"]- 273.15

# Сравниваем температуру из разных API-запросов
def test_temperature():
    assert temperature_celsius == pytest.approx(temperature_fromkelvin),f"Температура в кельвенах {temperature_fromkelvin}К не равна температуре в цельсиях {temperature_celsius}℃"
