def title_string():
    """ Функция получает на ввод строку
    и выводит первое слово
    с заглавной буквы"""
    my_title_string = str(input())
    title_string = my_title_string.title()
    return title_string


print(title_string())
print(title_string.__doc__)

