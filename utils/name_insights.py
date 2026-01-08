from popularity_of_the_name import load_names_from_file, get_gender, get_name_popularity, parse_popularity_data
from top_100_names import load_rating_from_file

#Объединяем написанные ранее функции в готовую программу
def main():
    print("Добро пожаловать в анализатор имён!")

    username = input('Введите имя с заглавной буквы: ').strip()
    result = get_name_popularity(username)
    if isinstance(result, str):
        print(result)
    else:
        rank, percent = parse_popularity_data(result.text, username)
        if rank is not None and percent is not None:
            print(f'Имя {username} занимает {rank} место по популярности в России. Приблизительно {percent}% людей являются носителями этого имени!')

    choice = input('Получить информацию топ-100 имен в России? (да/нет): ')
    if choice.lower() == 'да':
        load_rating_from_file()
    elif choice.lower() == 'нет':
        print('Благодарим за использование программы!')
    else:
        print('Ошибка. Введите ответ в формате "Да" или "Нет"')

if __name__ == '__main__':
    main()
