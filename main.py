# Получение данных от пользователя
while True:
    print("Введите 'y' для добавления данных, и 'n' для завершения")
    cheak: str = input()
    if cheak in ["y","Y","yes", "Yes" ,"YES"]:
        try:
            print('Введите ФИО и год рождения:')
            Surname, Name, Patronymic, Year = map(str, input().split())
            print(f"Вы ввели: {Surname} {Name} {Patronymic} {Year}")
            assert Year.isdigit()
        except ValueError:
            print('Не правильно внесены данные!')
        except:
            print('Ошибка!')
        # Запись данных в файл
        try:
            my_file = open("DataPeople.txt", "a", encoding='utf8')
            my_file.write(f"{Surname} {Name} {Patronymic} {Year}\n")
            my_file.close()
        except PermissionError:
            print('У вас нет доступа к данному файлу!')
        except:
            print('Ошибка!')
    else:
        exit()