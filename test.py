from prettytable import PrettyTable
myTable = PrettyTable(["Student Name", "Class", "Section", "Percentage"])

Surname, Name, Patronymic, Year = map(str, input().split())
# Add rows
myTable.add_row([Surname, Name, Patronymic, Year])

print(myTable)