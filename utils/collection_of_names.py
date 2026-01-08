import requests
import time
from bs4 import BeautifulSoup

#Парсим все страницы сайта с именами и сохраняем список имён в HTML
def parse_letter_with_pagination():
    all_names = []
    page = 1

    while True:
        url = f'https://popname.ru/names?&page={page}'
        response = requests.get(url)

        if response.status_code != 200:
            #print(f'Страница {page} не найдена: {response.status_code}')
            break

        result = BeautifulSoup(response.text, 'html.parser')
        column_name = result.find_all('div', class_='col-md-4')

        page_names = []
        for name in column_name:
            h5_tag = name.find('h5')
            if h5_tag:
                res = h5_tag.get_text(strip=True)
                page_names.append(res)

        if not page_names:
            #print(f"На странице {page} не найдено тегов h5 с именами")
            break

        all_names.extend(page_names)
        #print(f"Страница {page}: найдено {len(page_names)} имен. Всего собрано: {len(all_names)}")

        next_page = result.find('a', {'class': 'page-link', 'rel': 'next'})
        if not next_page:
            #print(f"Достигнута последняя страница ({page})")
            break

        page += 1
        time.sleep(0.3)

    return all_names

if __name__ == "__main__":
    parse = parse_letter_with_pagination()
    with open('all_names.html', 'w', encoding='utf-8') as f:
        for name in parse:
            f.write(name + '\n')

    print(f"Сохранено {len(parse)} имён")


