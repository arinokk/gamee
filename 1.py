import psycopg2

conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    database='thinktestdb',
    password='arina'
)
cursor = conn.cursor()
print("Database successfully connected!")


def insert_data_user(name, surname, email, password, birthdate):

    cursor.execute("INSERT INTO users (name, surname, email, password, birthdate) VALUES (%s, %s, %s, %s, %s)", (name, surname, email, password, birthdate))
    conn.commit()
insert_data_user('Arshak', 'Hakobyan', 'arjhakobyan@mail.ru', '1234567', '1987-03-07')
insert_data_user('Marianna', 'Galoyan', 'mariishgal@gmail.com', 'marishka', '1995-06-15')
insert_data_user('Gagik', 'Xachatryan', 'gag0000@mail.ru', '145gAg0o', '2001-11-30')