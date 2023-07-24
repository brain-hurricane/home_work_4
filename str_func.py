
def string_to_upper(string):
    """
    string to upper case 222
    """
    return string.upper()


def string_to_title(string):
    """
    делает заглавными первые буквы каждого слова в строке, поступившей на вход функции
    """

    string_list = string.split(" ")
    string_list_title = [s.title() for s in string_list]
    result = " ".join(string_list_title)

    return result
