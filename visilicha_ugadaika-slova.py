# Игра висилица. За вопросы не обессудте, на что фантазии хватило\0/
import random
word_list = [('Что происходит с мозгом когда долго сидишь за компом?', 'жопка'), ('Куда мужики ходят бухать?', 'рыбалка'), ('Где надо много копать?', 'дача')]

def get_word():
    random.shuffle(word_list)
    return random.choice(word_list)

def play():
    flag = False
    word = get_word()
    qwe, ans = word
    ans = ans.upper()
    word_completion = '_' * len(ans)    # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                      # сигнальная метка
    guessed_letters = []                 # список уже названных букв
    guessed_words = []                   # список уже названных слов
    tries = 6                            # количество попыток


    print(f"{'Давайте играть в угадайку слов!':*^60}")      # Выводим строку приветствие
    vivod_dannih_hader(tries, qwe, word_completion)         # Подключаем ввывод данных(виселица, попытки, слово, подсказки и т.д.)

    while guessed == False:
        letter = input('Введите букву или слово целиком: ').upper()
        print('*' * 40)

        while not letter.isalpha():
            print('Вы ввели не букву:(( Поробуйте еще раз')
            letter = input('Введите букву или слово целиком: ').upper()
            print('*' * 40)

        if letter == ans:
            print(f'Поздравляю, вы угадали слово! Загаданное слово - "{ans}"' )
            flag = igraem_eche_raz()  # Подключаем функцию - играем еще раз, ДА/НЕТ?
            guessed = flag
            break
        elif letter != ans and len(letter) > 1:
            print('Такого слова нет, попробуйте еще раз.  - 1 попытка!')
            tries -= 1
            guessed_words.append(letter)
            vivod_dannih_footer(tries, qwe, word_completion)
            if tries == 0:
                print('Попытки кончились, вы проиграли. Загаданное слово - ' + '"' + ans+ '"')
                flag = igraem_eche_raz() # Подключаем функцию - играем еще раз, ДА/НЕТ?
                guessed = flag
            continue


        word_completion = list(word_completion)
        indx = ans.find(letter)
        if letter in ans and len(letter) == 1 and letter not in guessed_letters:
            while indx != -1:
                word_completion[indx] = letter
                indx = ans.find(letter, indx + 1)
            vivod_dannih_footer(tries, qwe, word_completion)  # Подключаем ввывод данных(виселица, попытки, слово, подсказки и т.д.)
            guessed_letters.append(letter)


        elif letter in guessed_letters:
            print('Внимательней, такая буква уже была!'+'("'+letter+'") - 1 попытка!')
            tries -= 1
            vivod_dannih_footer(tries, qwe, word_completion)  # Подключаем ввывод данных(виселица, попытки, слово, подсказки и т.д.)
            if tries == 0:
                print('Попытки кончились, вы проиграли. Загаданное слово - ' + '"' + ans+ '"')
                flag = igraem_eche_raz() # Подключаем функцию - играем еще раз, ДА/НЕТ?
                guessed = flag


        else:
            print('Такой буквы нет, попробуйте еще раз.  - 1 попытка!')
            tries -= 1
            vivod_dannih_footer(tries, qwe, word_completion)  # Подключаем ввывод данных(виселица, попытки, слово, подсказки и т.д.)
            if tries == 0:
                print('Попытки кончились, вы проиграли. Загаданное слово - ' + '"' + ans+ '"')
                flag = igraem_eche_raz() # Подключаем функцию - играем еще раз, ДА/НЕТ?
                guessed = flag

        if word_completion == list(ans):
            print('Поздравляю, вы угадали слово!')
            flag = igraem_eche_raz() # Подключаем функцию - играем еще раз, ДА/НЕТ?
            guessed = flag

def vivod_dannih_hader(tries, qwe, word_completion):
    visilicha = display_hangman(tries)
    popitki = f'У Вас есть {tries} попыток!'
    podskazka = f'Подсказка: {qwe}'
    print(f"И так загаданное слово - '{word_completion:^{len(word_completion)}}'  {podskazka}  ({popitki:>{len(popitki)}}) ")   # Выводим строку вывода висилици и попыток
    print(visilicha)

def vivod_dannih_footer(tries, qwe, word_completion):
    visilicha = display_hangman(tries)
    podskazka = f'Подсказка: {qwe}'
    popitki = f'У Вас осталось {tries} попыток/ки!'
    print(f"И так загаданное слово - '{''.join(word_completion):^{len(word_completion)}}'  {podskazka}  ({popitki:>{len(popitki)}}) ")  # Выводим строку вывода висилици и попыток
    print(visilicha)

def igraem_eche_raz():
    povtor = input('Вы хотите сыграть еще? Введите "Да" или "Нет"').lower()
    while povtor != 'да':
        if povtor == 'нет':
            print('До свидания!!')
            flag = True
            return  flag
            #break
        else:
            print('Ведите только "Да" или "Нет"')
            povtor = input('Вы хотите сыграть еще? Введите "Да" или "Нет"').lower()
            #continue

    if povtor == 'да':
            play()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
    '''
    --------
    |      |
    |      
    |    
    |      
    |     
    -
    '''
    ]
    return stages[tries]

play()

