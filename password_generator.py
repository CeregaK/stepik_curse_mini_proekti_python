# Генератор паролей
import random
digits = '0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_.><{}][/\\'
chars = []
password = []
selekt1 = ['digits_in','uppercase_letters_in','lowercase_letters_in','punctuation_in']
selekt2 = [digits,uppercase_letters,lowercase_letters,punctuation]
selekt3 = ['цифры','прописные буквы','строчные буквы','спец-символы']

lenght = int(input('Введите длину пароля: '))

def get_password(password, chars, lenght):
    if len(chars) != 0:
        password += random.sample(chars, lenght)
        return f"Длина пароля: {len(password)}, Пароль: {''.join(password)}"
    else:
        return f'Пароль не может быть пустым! Включите хоть один пункт.'


def yes_or_not(selekt1, selekt2, selekt3, chars):
    for el in range(len(selekt1)):
        while True:
            selekt1[el] = input(f'Включать {selekt3[el]} (да или нет)')
            if selekt1[el].lower() == 'да':
                chars.extend(selekt2[el])
                #print(chars)
                break
            elif selekt1[el].lower() == 'нет':
                break
            else:
                print('Введите только "да" или "нет"!')
                continue

yes_or_not(selekt1, selekt2, selekt3, chars)

for _ in range(lenght + 1):
    random.shuffle(chars)

print('=' * 40)
print(get_password(password, chars, lenght))
print('=' * 40)
