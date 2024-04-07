


def main():
    while True:
        print ('1 -  Добавить запись')
        print('0 - выйти из программы')
        print('Введите номер пункта меню ', end ='')
        menuItem= int(input ().strip())

        match menuItem:

            case 0:
                print("Выход... ")
                break

            case 1:
                print(f"Команда  {menuItem}")
            case _:
                print("Неверная команда")


if __name__ == '__main__':
        main()