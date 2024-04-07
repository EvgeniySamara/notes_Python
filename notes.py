import datetime
import csv
import os


class Notes:
    notesList = []

    def __init__(self):
        Notes.notesList.append(dict(noteid= 'id', txt = 'Заметка', tag = 'Тэги', Notedt = "Дата и время изменения"))

    @staticmethod
    def addNote(txt, tag=None):
        noteid = len(Notes.notesList)
        dt_now = datetime.datetime.now()
        dt_string = dt_now.strftime('%d/%m/%y %H:%M:%S')
        if tag is None:
            tag = []
        d = dict(noteid= noteid, txt = txt, tag = tag, Notedt = dt_string)

        Notes.notesList.append(d)

    @staticmethod
    def listNotes():
        for c in Notes.notesList:
            print(*c.values(), sep ='   ')


class FileInOut:

    @staticmethod
    def toCsv(outdict,filename = 'notes_file.csv'):
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csv_file:


                fieldnames = outdict[0].keys()
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(outdict)
                print('Файл сохранен успешно')
        except Exception as e:
            print('При сохранении возникла ошибка '+str(e))


    @staticmethod
    def fromCsv(file_name='note_book.csv'):
        if os.path.exists(file_name):
            with open('name.csv') as csvfile:
                reader = csv.DictReader(csvfile)


def main():
    notes = Notes()
    files = FileInOut()
    while True:
        print('1 -  Добавить запись')
        print('2 -  Удалить запись')
        print('3 -  Редактировать запись')
        print('4 -  Загрузить из файла')
        print('5 -  Сохранить в файл')
        print('6 -  Просмотреть записи')
        print('0 - выйти из программы')
        print('Введите номер пункта меню ', end='')
        menuItem = int(input().strip())

        match menuItem:

            case 0:
                print("Выход... ")
                break

            case 1:
                print("Введите текст заметки ", end='')
                notes.addNote(input())
                notes.listNotes()
            case 5:
                files.toCsv(Notes.notesList)
            case 6:
                notes.listNotes()
            case _:
                print("Неверная команда")


if __name__ == '__main__':
    main()
