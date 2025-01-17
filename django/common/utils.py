import re



def remove_chars(chars_remove, string):
    return re.sub(chars_remove, '', string)