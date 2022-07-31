from datetime import datetime
import random


def main():
    choice = input("Введіть цифу, відповідно до вашого вибору.\n1 - створити пароль для нового сервісу."
               "\n2 - отримати пароль від сервісу, якщо він вже створений.\n")

    db_file = open("db.txt", "r+")
    db = db_file.read()

    def db_writer(service_name, password):
        if db == "":
            db_file.write(service_name + " " + str(password))
        else:
            db_file.write("\n" + service_name + " " + str(password))

    def new_service():
        service_name = input("Введіть назву сервісу, для якого потрібно створити пароль:\n")

        current_time = datetime.today()

        str_current_time = ""
        for i in str(current_time):
            if i != "-" and i != "." and i != ":" and i != " ":
                str_current_time += i

        password = str_current_time + service_name

        password = list(password)

        random.shuffle(password)

        del password[1:4]

        password.append(random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

        str_password = ''.join(map(str, password))

        print("Пароль створено і збережено до бази: " + str_password)

        db_writer(service_name, str_password)

        exit = input("Для завершення нажміть будь-яку клавішу")

    def find_service_password():
        service_name = input("Введіть назву сервісу, до якого хочете отримати пароль.\n")

        services_data = db.split('\n')
        success_marker = 0
        for i in services_data:
            j = i.split(" ")
            if service_name in j[0]:
                success_marker = 1
                print("Пароль: " + j[1])

        if success_marker == 0:
            print("У базі немає даних про цей сервіс!")

        exit = input("Для завершення нажміть будь-яку клавішу")

    if choice == "1":
        new_service()
    elif choice == "2":
        find_service_password()
    else:
        print("Неправильно введено вибір!")


if __name__ == "__main__":
    main()