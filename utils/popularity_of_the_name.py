import requests
from bs4 import BeautifulSoup

def load_names_from_file(): #Получаем файл с именами
    with open('all_names.html', 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def get_gender(name): #Определяем пол по имени
    endings = ['ь', 'а', 'я']
    if name[-1].lower() in endings:
        return 'female'
    else:
        return 'male'

def get_name_popularity(name): #Получаем имя и запрашиваем информацию у сайта
    all_names = load_names_from_file()
    if name in all_names:
        gender = get_gender(name)
        url = f'https://popname.ru/pop-name?query={name}&gender={gender}'
        response = requests.get(url)
        return response
    else:
        return f'Имя {name} не найдено. Похоже, Вы единственный носитель этого имени.'

def parse_popularity_data(html_text, name): #Получаем информацию о популярности
    soup = BeautifulSoup(html_text, 'html.parser')
    data_block = soup.find('div', class_='d-inline-block m-3')
    if data_block is None:
        return None, None
    spans = data_block.find_all('span', style=True)

    rank_text = None
    percent_text = None

    if len(spans) >= 1:
        rank_spans = spans[0]
        rank_text = rank_spans.get_text(strip=True)

    if len(spans) >= 2:
        percent_spans = spans[1]
        percent_text = percent_spans.get_text(strip=True)

    rank = None
    percent = None

    if rank_text:
        rank_res = rank_text.strip('#')
        rank = int(rank_res)

    if percent_text:
        percent_res = percent_text.strip('%')
        percent = float(percent_res)

    return rank, percent

if __name__ == "__main__":
    username = input('Введите имя с заглавной буквы: ').strip()
    result = get_name_popularity(username)

    if isinstance(result, str):
        print(result)
    else:
        rank, percent = parse_popularity_data(result.text, username)
        if rank is not None and percent is not None:
            print(f'Имя {username} занимает {rank} место по популярности в России. Приблизительно {percent}% людей являются носителями этого имени!')



