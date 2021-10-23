import random as rand

class Generator:
    def generator():
        i = 0
        while i < 100:
            print('Какой длинны вам нужен пароль ?')
            lenght_password = int(input())
            if lenght_password >= 5 and lenght_password <= 20:
                cipher_list_start = []
                cipher_list_finish = []
                i = 0
                while i < lenght_password:
                    char_numb = rand.randint(65, 122)
                    char_a = chr(char_numb)
                    cipher_list_start.append(char_a)
                    i += 1

                for j in cipher_list_start:
                    result = j
                    cipher_list_finish.append(result)

                finish_is_cipher = ''.join(cipher_list_finish)

                print(finish_is_cipher)

                print('Сохранить его в файл(1 - да, 0 - нет)?')

                choise_numb = int(input())

                if choise_numb == 1:
                    for i in range(0, 10):
                        with open('password.txt', 'w') as filehandle:
                            for listitem in cipher_list_finish:
                                filehandle.write(listitem)
                elif choise_numb == 0:
                    break
                else:
                    print('Других вариантов нету!')
                    break
                break
            else:
                print('Не подходящая длинна =_- ! Пробуем ещё раз\n')
                i += 1

    generator()