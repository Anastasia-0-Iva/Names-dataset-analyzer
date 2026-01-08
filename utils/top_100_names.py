from bs4 import BeautifulSoup

#Получаем и выводим рейтинг топ-100 имён в РФ, скаченные из API в HTML
def load_rating_from_file():
    with open('popname_rating.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    name_links = soup.select('table a')
    top_names = [link.get_text(strip=True) for link in name_links]

    gender_cells = soup.select('table tr td:nth-of-type(3)')
    gender_info = [link.get_text(strip=True) for link in gender_cells]

    popularity_cells = soup.select('table tr td:nth-of-type(4)')
    percentage_of_popularity = [link.get_text(strip=True) for link in popularity_cells]

    print('ТОП-100 имен:')

    for count, name in enumerate(top_names, 1):
        gender = gender_info[count - 1]
        percent = percentage_of_popularity[count - 1]
        print(f'{count}. {name} - {gender}. (Приблизительный процент носителей: {percent})')

if __name__ == "__main__":
    load_rating_from_file()

