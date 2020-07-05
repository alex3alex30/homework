def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть "/catalog/"
    """
    result_list  = []
    for link in url_list:
        if '/catalog/' in link:
            result_list.append(link)
    return result_list
    """return [link for link in result_list if '/catalog/' in link]"""


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).

    >>> get_str_center("foobar")
    'ob'
    """
    middle = len(input_str) // 2
    if len(input_str) % 2 == 1:
        output_str = input_str[middle - 1:middle + 2]
    else:
        output_str = input_str[middle - 1:middle + 1]
    return output_str


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    import collections

    output_dict = collections.Counter(input_str)
    return output_dict


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    middle = len(str1) // 2
    result_str = str1[:middle] + str2 + str1[middle:]
    return result_str
    result = list(str1)  # O(n) Omem(n)
    list2 = list(str2)  # O(m) Omem(m)
    result[middle:middle] = list2  # O(m)??
    return ''.join(result)  # O(n + m) Omem(n + m)  # Omem(n+m)


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    # your code here
    even_int_list = list(range(0,101,2))
    even_int_list = [ num for num in range(101) if num % 2 == 0]
    return even_int_list
