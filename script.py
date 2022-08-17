from turtle import update
import psycopg2

class PSYCOPG_2:

    def __init__(self, datab :str, name :str, password :str) -> None:
        self.connection = psycopg2.connect(database = datab, user = name, password = password)

    # Функция, создающая структуру БД (таблицы)
    def creating(self):

        with self.connection.cursor() as cur:
            cur.execute('''CREATE TABLE IF NOT EXISTS employee(
                employee_id SERIAL PRIMARY KEY, 
                name varchar(60) NOT NULL, 
                surname varchar(60) NOT NULL, 
                email varchar(60)
            );
            ''')
            cur.execute('''CREATE TABLE IF NOT EXISTS phone(
                number varchar(12) PRIMARY KEY, 
                employee_id integer references employee(employee_id),
                ordinal integer not null
            );
            ''')

        self.connection.commit()


    # Вспомогательная функция для загрузки данных
    def inserting_data(self):

        with self.connection.cursor() as cur:
            cur.execute("""INSERT INTO employee(name, surname, email)
                VALUES  ('Наталья', 'Аристова', 'Lazulit@yandex.ru'),
                        ('Наталия', 'Афанасьева', 'afanasjewa.nataliya2013@yandex.ru'),
                        ('Татьяна', 'Бабская', 'cortez.90@mail.ru'),
                        ('Светлана', 'Бакулина', 'Mama.espana.inst@yandex.ru'),
                        ('Светлана', 'Башлыкова', '9031121217@mail.ru'),
                        ('Анна', 'Березань', 'y125@mail.ru'),
                        ('Лидия', 'Бунина', 'Lidabunina@rambler.ru'),
                        ('Ирина', 'Гаевая', 'Gaevayain77@gmail.com'),
                        ('Марина', 'Дедусси', 'markis22@yandex.ru'),
                        ('Наталья', 'Дементьева', 'Dementevana71@mail.ru'),
                        ('Ольга', 'Ивочкина', 'fox2lv54@yandex.ru'),
                        ('Ирина', 'Квасникова', 'kwasnickova.irina@yandex.ru'),
                        ('Нина', 'Ковалева', 'Kovaleva.55@list.ru'),
                        ('Екатерина', 'Кудинова', 'katja-istra07@yandex.ru'),
                        ('Марина', 'Лащевская', 'Azhakina@ya.ru'),
                        ('Ирина', 'Лушникова', 'lugnikova@mail.ru'),
                        ('Татьяна', 'Майшева', 'tennis-city63@mail.ru'),
                        ('Лилия', 'Мамонова', 'Ladyli05@mail.ru'),
                        ('Энфиса', 'Муллагалимова', 'enfisa@mail.ru'),
                        ('Наталья', 'Наумова', 'Kadry@sis-d.ru'),
                        ('Людмила', 'Николаевна', 'k.rf1960@yandex.ru'),
                        ('Ирина', 'Плужник', 'pluzhnikii@yandex.ru'),
                        ('Ольга', 'Рахматулина', 'rahmatulina_olga@mail.ru'),
                        ('Екатерина', 'Реунова', 'revant@mail.ru'),
                        ('Ирина', 'Родионова', 'irina_rodionova7@mail.ru'),
                        ('Светлана', 'Cавельева', 'savelyeva15121966@mail.ru'),
                        ('Юлия', 'Сенина', 'yu_l_ya@mail.ru'),
                        ('Анна', 'Слащенко', 'anya.zh81@mail.ru'),
                        ('Надежда', 'Смертина', 'nadezhda_smertin@mail.ru'),
                        ('Тамара', 'Снеткова', 'Tamara-nik@mail.ru'),
                        ('Наталья', 'Сургутова', 'surgutova.natalia@gmail.com'),
                        ('Римма', 'Тетерина', 'tet-rimma@yandex.ru'),
                        ('Елена', 'Титова', 'titovaelena1973@yandex.ru'),
                        ('Анна', 'Толстая', 'tolstaya.an@yandex.ru'),
                        ('Елена', 'Хилькова', 'khilkovabortnik74@gmail.com'),
                        ('Елена', 'Хотченко', 'kras.2564@mail.ru'),
                        ('Оксана', 'Храмцова', 'xramcova73@gmail.com'),
                        ('Анна', 'Черненко', 'annet-pattinson@yandex.ru'),
                        ('Наталья', 'Шпилевская', 'airwizard@mail.ru');
            """)
            cur.execute("""INSERT INTO phone(number, employee_id, ordinal)
                VALUES  ('79162065661', 1, 1),
                        ('79035585130', 1, 2),
                        ('79779186215', 1, 3),
                        ('79109873718', 2, 1),
                        ('79162129798', 3, 1),
                        ('79183096376', 4, 1),
                        ('79031121217', 5, 1),
                        ('79222801701', 6, 1),
                        ('79138893628', 7, 1),
                        ('79215120561', 7, 2),
                        ('79219059986', 8, 1),
                        ('79199241283', 9, 1),
                        ('79500055155', 10,, 1),
                        ('79260442480', 12, 1),
                        ('79191030033', 13, 1),
                        ('79037311242', 14, 1),
                        ('79171280563', 15, 1),
                        ('79788123257', 16, 1),
                        ('79128707991', 16, 2),
                        ('79779043247', 17, 1),
                        ('79653844533', 18, 1),
                        ('79213984365', 19, 1),
                        ('79124005800', 20, 1),
                        ('79211515823', 21, 1),
                        ('79520408015', 21, 2),
                        ('79005608387', 21, 3),
                        ('79876455766', 21, 4),
                        ('79211614880', 22, 1),
                        ('79502000237', 23, 1),
                        ('79266442796', 25, 1),
                        ('79151420077', 26, 1),
                        ('79835074741', 27, 1),
                        ('79827186284', 31, 1),
                        ('79224190028', 32, 1),
                        ('79671580441', 34, 1),
                        ('79032743707', 35, 1),
                        ('79102554499', 36, 1),
                        ('79376973499', 38, 1),
                        ('89841468992', 39, 1);
                """)

            self.connection.commit()


    # Функция, позволяющая добавить нового клиента
    def add_new_client(self, name, surname, mail, *phones):

        with self.connection.cursor() as cur:
            cur.execute("""INSERT INTO employee(name, surname, email)
                VALUES (%s, %s, %s)
                RETURNING employee_id;
            """, (name, surname, mail))
            new_client = cur.fetchone()

            for ordinal, number in enumerate(phones):
                    cur.execute("""INSERT INTO phone(number, employee_id, ordinal)
                        VALUES (%s, %s, %s);
                    """, (number, new_client, ordinal+1))
            self.connection.commit()


    # Функция, позволяющая добавить телефон для существующего клиента
    def add_phone_for_existing_client(self, client_id, *phones):

        with self.connection.cursor() as cur:
            cur.execute("""SELECT * from phone WHERE employee_id = %s""", (client_id,))
            ordinal_length = len(cur.fetchall())
            for ordinal, number in enumerate(phones, ordinal_length+1):
                    cur.execute("""INSERT INTO phone(number, employee_id, ordinal)
                        VALUES (%s, %s, %s);
                    """, (number, client_id, ordinal))
        
            self.connection.commit()


    # Функция, позволяющая изменить данные о клиенте
    def editing_client(self, client_id, first_name=None, last_name=None, email=None, *phones):
        with self.connection.cursor() as cur:
            cur.execute("""UPDATE employee SET name=%s, surname=%s, email =%s WHERE employee_id=%s;""", (first_name, last_name, email, client_id))


            for ordinal, number in enumerate(phones):
                cur.execute("""UPDATE phone SET number=%s WHERE employee_id=%s AND ordinal = %s;""", (number, client_id, ordinal+1))

            self.connection.commit()


    # Функция, позволяющая удалить телефон для существующего клиента
    def delete_phone_number(self, client_id, *phone):

        with self.connection.cursor() as cur:
            for number in phone:
                cur.execute("""DELETE from phone WHERE number=%s AND employee_id=%s;""", (number, client_id))

            self.connection.commit()


    # Функция, позволяющая удалить существующего клиента
    def delete_client(self, client_id):

        with self.connection.cursor() as cur:

            cur.execute("""DELETE from phone WHERE employee_id=%s;""", (client_id, ))
            cur.execute("""DELETE from employee WHERE employee_id=%s;""", (client_id, ))

            self.connection.commit()


    # Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
    def find_client(self, first_name="%", last_name="%", email="%", phone=None):
        with self.connection.cursor() as cur:
            if phone is not None:
                cur.execute("""SELECT employee_id from phone WHERE number=%s;""", (phone, ))
                result = cur.fetchone()
                id = result[0] if result is not None else 0

                cur.execute("""SELECT * from employee WHERE employee_id = %s;""", (id, ))
                print(cur.fetchall())
            else:
                cur.execute("""SELECT * from employee WHERE name LIKE %s AND surname LIKE %s AND email LIKE %s;""", (first_name, last_name, email))
                print(cur.fetchall())


    def closing(self):
        self.connection.close()
database, user, password = input('Введите название БД: '), input('Введите логин от postgres: '), input('Введите пароль от postgres: ')
test = PSYCOPG_2('func_db', 'postgres', 'Akametop130499')
#test.creating()
#test.inserting_data()
#test.add_new_client('Олег', 'Кравцов', 'oleg@list.ru', '79033884455', '79511445579')
#test.add_phone_for_existing_client(36, '79887541232', '79246547890')
#test.editing_client(47, 'Иван', 'Огайнов', '777', '888')
#test.delete_phone_number(46, '777', '888')
#test.delete_client(46)
#test.find_client(first_name='Анна', phone='79215120561')
test.closing()