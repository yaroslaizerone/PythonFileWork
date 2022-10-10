from prettytable import PrettyTable
try:
    myTable = PrettyTable(["Surname", "Name", "Patronymic", "Year"])
    my_file = open("DataPeople.txt", encoding='utf8')
    s: list = my_file.readlines()
    a: int = 0
    while a < len(s):
        line: str = len(s[a])

        if a + 1 == len(s):
            Surname, Name, Patronymic, Year = map(str, s[a].split())
            myTable.add_row([Surname, Name, Patronymic, Year])
        else:
            Remove_last: str = s[a][:line - 1]
            Surname, Name, Patronymic, Year = map(str, Remove_last.split())
            myTable.add_row([Surname, Name, Patronymic, Year])
        a += 1
    print(myTable)
except SyntaxError:
    print("Ошибка чтения файла!")
except:
    exit()