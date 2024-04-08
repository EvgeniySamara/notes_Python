import datetime
import csv
import os


class Notes:
    notesList = []

    def __init__(self):
        Notes.notesList.append(dict(noteid='id', txt='Заметка', tag='Тэги', Notedt="Дата и время изменения"))

    @staticmethod
    def addNote(txt, tag=None):
        noteid = len(Notes.notesList)
        if tag is None:
            tag = []
        else:
            tag = list(map(lambda x: x.strip(), tag.split(',')))
        d = dict(noteid=noteid, txt=txt, tag=tag, Notedt=Notes.getDT())

        Notes.notesList.append(d)

    @staticmethod
    def listNotes():
        for c in Notes.notesList:
            print(*c.values(), sep='   ')

    @staticmethod
    def getDT():
        dt_now = datetime.datetime.now()
        dt_string = dt_now.strftime('%d/%m/%y %H:%M:%S')
        return dt_string

    @staticmethod
    def editNotes(noteid):
        for i in range(1, len(Notes.notesList)):
            if int(Notes.notesList[i]['noteid']) == noteid:
                break
        print("Введите, что будем редактировать: текст заметки(1), теги(2) ", end='')
        chid = int(input().strip())
        match chid:
            case 1:
                print("Введите текст заметки: ", end='')
                Notes.notesList[i]['txt'] = input().strip()
                Notes.notesList[i]['Notedt'] = Notes.getDT()

                print("Текст заметки изменен")
            case 2:
                print("Введите теги через запятую: ", end='')

                Notes.notesList[i]['tag'] = list(Notes.notesList[i]['tag'])
                Notes.notesList[i]['tag'] = list(map(lambda x: x.strip(), input().split(',')))
                Notes.notesList[i]['Notedt'] = Notes.getDT()

                print("Тэги изменены")
            case _:
                print("Неверная команда")

    @staticmethod
    def delNotes(noteid):
        for i in range(1, len(Notes.notesList)):
            if int(Notes.notesList[i]['noteid']) == noteid:
                del Notes.notesList[i]
                print("Удалено успешно")
                break

    @staticmethod
    def getNotesbyDate(notesdate):
        for i in range(1, len(Notes.notesList)):
            if Notes.notesList[i]['Notedt'][:8] == notesdate:
                print(*Notes.notesList[i].values())

    @staticmethod
    def getNotesbyId(notesid):
        if len(notesid) > 0:
            for i in notesid:
                print(*Notes.notesList[int(i)].values())


class FileInOut:

    @staticmethod
    def toCsv(outdict, filename='notes_file.csv'):
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csv_file:

                fieldnames = outdict[0].keys()
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(outdict)
                print('Файл сохранен успешно')
        except Exception as e:
            print('При сохранении возникла ошибка ' + str(e))

    @staticmethod
    def fromCsv(file_name='note_book.csv'):
        if os.path.exists(file_name):
            try:
                with open(file_name, encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile)

                    Notes.notesList.clear()
                    Notes.notesList = list(reader)

                    print('Данные успешно загружены')

            except Exception as e:
                print('При загрузке данных возникла ошибка ' + str(e))
        else:
            print(f"Файл {file_name} не найден")


def main():
    notes = Notes()
    files = FileInOut()
    while True:
        print()
        print('Основное меню')
        print('1 -  Добавить запись')
        print('2 -  Удалить запись')
        print('3 -  Редактировать запись')
        print('4 -  Загрузить из файла')
        print('5 -  Сохранить в файл')
        print('6 -  Просмотреть записи')
        print('7 -  Вывести записи за дату')
        print('8 -  Вывести записи по id')
        print('0 -  Выйти из программы')
        print('Введите номер пункта меню ', end='')
        menuItem = int(input().strip())

        match menuItem:

            case 0:
                print("Выход... ")
                break

            case 1:
                print("Введите текст заметки ", end='')
                txt = input().strip()
                print("Введите теги через запятую (необязательный параметр): ", end='')
                tag = input()
                notes.addNote(txt, tag)

                notes.listNotes()
            case 2:
                notes.listNotes()
                print("Введите номер заметки для удаления ", end='')
                chid = int(input().strip())
                Notes.delNotes(chid)
                notes.listNotes()

            case 3:
                notes.listNotes()
                print("Введите номер заметки для редактирования ", end='')
                chid = int(input().strip())
                Notes.editNotes(chid)

            case 4:
                files.fromCsv('notes_file.csv')
            case 5:
                files.toCsv(Notes.notesList)
            case 6:
                notes.listNotes()
            case 7:
                print("Введите дату в формате дд/мм/гг")
                notes.getNotesbyDate(input().strip())
            case 8:
                print("Введите id заявок через запятую")
                notes.getNotesbyId(input().split(','))
            case _:
                print("Неверная команда")


if __name__ == '__main__':
    main()
