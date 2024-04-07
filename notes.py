import datetime


class Notes:
    id = 0
    notesList = {}

    def __init__(self, txt):
        Notes.id += 1
        self.id = Notes.id
        dt_now = datetime.datetime.now()
        dt_string = dt_now.strftime('%d/%m/%y %H:%M:%S')
        Notes.notesList[self] = [txt, dt_string]



def main():
    while True:
        print('1 -  Добавить запись')
        print('0 - выйти из программы')
        print('Введите номер пункта меню ', end='')
        menuItem = int(input().strip())

        match menuItem:

            case 0:
                print("Выход... ")
                break

            case 1:
                print("Введите текст заметки ", end='')
                note = Notes(input())
                print(f" Номер {note.id}")
                print(Notes.notesList)
            case _:
                print("Неверная команда")

if __name__ == '__main__':
    main()
