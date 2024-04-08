import requests

# Параметры запроса
params = {

    "url": "https://www.apple.com",   # ссылка на сайт, где нужно сделать скриншот
    "viewport": "2560x1440",    # разрешение
}

# URL для запроса
url = "http://api.screenshotlayer.com/api/capture"

# Отправка GET-запроса к API Screenshotlayer
response = requests.get(url, params=params)

if response.status_code == 200:
    # Сохраняем полученное изображение на диск
    with open("screenshot.png", "wb") as file:
        file.write(response.content)
    print("Снимок экрана веб-страницы сохранен ")
else:
    print("Ошибка при получении снимка экрана. Код ответа:", response.status_code)