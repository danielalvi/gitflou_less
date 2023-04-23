def upper_string():
    """Функция получает строку и выводит ее 
    заглавными буквами
    """
    my_string = str(input())
    up_string = my_string.upper()
    return up_string

print(upper_string())
print(upper_string.__doc__)
