import requests

API_key = '995fa1c5b9649503a3386aca1d3e32a4'
city_name = 'Saint Petersburg'
limit = 1

#http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_key}

# Формируем URL для запроса
Standard_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
Metric_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"
Imperial_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=imperial"

# Отправляем GET-запрос
responseStandard = requests.get(Standard_url)
responseMetric = requests.get(Metric_url)
#responseImperial = requests.get(Imperial_url)

# Проверяем статус ответа
if responseMetric.status_code == 200:
    # Парсим JSON-ответ
    data_Metric = responseMetric.json()

    # Проверяем, есть ли данные
    if data_Metric:
        # Извлекаем данные
        city = data_Metric["name"]
        country = data_Metric["sys"]["country"]
        temperature = data_Metric["main"]["temp"]

        # Выводим информацию
        print(f"Город: {city}, {country}")
        print(f"Температура: {temperature}℃")
        temperature_celsius = temperature
    else:
        print("Город не найден.")
else:
    print(f"Ошибка: {responseMetric.status_code}")
    print(responseMetric.text)  # Выводим текст ошибки, если есть

# Проверяем статус ответа
if responseStandard.status_code == 200:
    # Парсим JSON-ответ
    data_Standard = responseStandard.json()

# Проверяем, есть ли данные
    if data_Standard:
        # Извлекаем данные
        city = data_Standard["name"]
        country = data_Standard["sys"]["country"]
        temperature = data_Standard["main"]["temp"]

        # Выводим информацию
        print(f"Город: {city}, {country}")
        print(f"Температура: {temperature}K")
    else:
        print("Город не найден.")
else:
    print(f"Ошибка: {responseStandard.status_code}")
    print(responseStandard.text)  # Выводим текст ошибки, если есть

temperature_fromkelvin = temperature - 273.15
temperature_fromkelvin = round(temperature_celsius,2)
print(f"Температурв в {temperature_fromkelvin}℃ равна температуре в {temperature}K")

if(temperature_celsius == temperature_fromkelvin):
    print(f"Запрос первой температуры в {temperature}K равен второму запросу температуры в {temperature_celsius}℃")
else:
    print(f"Запрос первой температуры в {temperature}K не равен второму запросу температуры в {temperature_celsius}℃")