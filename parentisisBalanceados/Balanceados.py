import re


def validate(got, expected):
    if got == expected:
        return True
    else:
        return False


def parentesis_coherentes(cadena=''):
    expected = [['(', ')'], ['[', ']'], ['{', '}']]
    balanceados = False
    clean_string = re.findall(r'([\[\]\{\}\(\) ])', cadena.replace(" ", ""))
    restart = True
    if cadena == '':
        return True
    else:
        while restart:
            for x in range(0, len(clean_string)):
                if clean_string[x] == expected[0][1] \
                        or clean_string[x] == expected[1][1] \
                        or clean_string[x] == expected[2][1]:

                    if [clean_string[x - 1], clean_string[x]] == expected[0] \
                            or [clean_string[x - 1], clean_string[x]] == expected[1] \
                            or [clean_string[x - 1], clean_string[x]] == expected[2]:

                        balanceados = True
                    else:
                        balanceados = False
                        x = len(clean_string) + 1
                        break

                    clean_string = clean_string[0:x - 1:] + clean_string[x + 1::]
                    break

            if x >= len(clean_string) or len(clean_string) == 1:
                restart = False
            elif not (expected[0][1] in clean_string
                      and expected[1][1] in clean_string
                      and expected[0][1] in clean_string):

                clean_string = clean_string[0:x:] + clean_string[x + 1::]

        return balanceados
