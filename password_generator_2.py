import random
import string
upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
digits = string.digits
punctuation = string.punctuation
stop ='LlOo1Ii0\\.\'\"'

def generate_password(length):
    temp = []
    words = [el for el in (upper_case + lower_case + digits) if el not in stop]
    a = [el for el in upper_case if el not in stop]
    b = [el for el in lower_case if el not in stop]
    c = [el for el in digits if el not in stop]
    d = [el for el in punctuation if el not in stop]
    random.shuffle(words)
    random.shuffle(a)
    random.shuffle(b)
    random.shuffle(c)
    random.shuffle(d)
    if length < 4:
        print('Пароль не может быть меньше трех символов')
    elif length == 4:
        temp.extend(random.choice(a) + random.choice(b) + random.choice(c) + random.choice(d))
    elif length > 4:
        temp.extend(random.choice(a) + random.choice(d) + random.choice(b) + random.choice(c) + random.choice(d))
        temp += random.sample(words, length - 5)
    random.shuffle(temp)
    passw = ''.join(temp)
    return passw

def generate_passwords(count, length):
    password = []
    while count > len(password):
        data = generate_password(length)
        if data not in password:
            password.append(data)
    print(*password, sep = '\n')



while True:
    flag = False
    count, length = int(input('Сколько сгенирировать паролей?: ')), int(input('Введите длину пароля: '))
    print('*' * (length + 5))
    generate_passwords(count, length)
    print('*' * (length + 5))

    text = input("Ещё раз?(да|нет): ")
    print('-' * (length + 5))
    if text == 'нет':
        print('exit program, goodbay')
        break
    while text != 'да':
        print('Введите только "да" или "нет"')
        text = input("Ещё раз?(да|нет): ")
        print('-' * (length + 5))
        if text == 'нет':
            flag = True
            break
    if flag == True:
        print('exit program, goodbay')
        break

