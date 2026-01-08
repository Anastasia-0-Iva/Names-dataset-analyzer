import requests

url_name = 'https://popname.ru/names' # Все имена
url_pop = 'https://popname.ru/pop-name' # Популярные имена
url_rating = 'https://popname.ru/rating-100-names' # Рейтинги имен

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    response_name = requests.get(url_name, headers=headers, timeout=10)
    response_name.raise_for_status()

    response_pop = requests.get(url_pop, headers=headers, timeout=10)
    response_pop.raise_for_status()

    response_rating = requests.get(url_rating, headers=headers, timeout=10)
    response_rating.raise_for_status()


    html_name = response_name.text
    print("HTML страница получена успешно")
    html_pop = response_pop.text
    print("HTML страница получена успешно")
    html_rating = response_rating.text
    print("HTML страница получена успешно")

    with open('popname.html', 'w', encoding='utf-8') as f:
        f.write(html_name)
    with open('popname_pop.html', 'w', encoding='utf-8') as f_pop:
        f_pop.write(html_pop)
    with open('popname_rating.html', 'w', encoding='utf-8') as f_rating:
        f_rating.write(html_rating)


except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе: {e}")