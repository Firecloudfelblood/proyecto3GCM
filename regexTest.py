import re


def clear(string):
    new = re.findall(r'([\[\]\{\}\(\)])', string)
    print(new)


print(clear('a(a[aa{d}g245]g)2345$'))