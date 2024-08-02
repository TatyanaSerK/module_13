import sqlite3



def initiate_db():

    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,    
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    # for i in range (1,5): #
    #     cursor.execute("INSERT INTO Products (title, description, price) VALUES (?,?,?)",
    #                    (f"Продукт{i}", f"описание {i}", f"{100*i}"))
    connection.commit()
    connection.close()

    connection2 = sqlite3.connect("users.db")
    cursor2 = connection2.cursor()
    cursor2.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL        
        )
        ''')
    connection2.commit()
    connection2.close()

# get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
def get_all_products():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products ")
    products = cursor.fetchall()
    return products


# # add_user(username, email, age), которая принимает: имя пользователя, почту и возраст.
def add_user(username, email, age):
    # Данная функция должна добавлять в таблицу Users вашей БД запись с переданными данными.
    # Баланс у новых пользователей всегда равен 1000. Для добавления записей в таблице используйте SQL запрос.
    connection2 = sqlite3.connect("users.db")
    cursor2 = connection2.cursor()
    cursor2.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)", (username, email, age, 1000))
    connection2.commit()


# is_included(username) принимает имя пользователя и возвращает True, если такой пользователь есть
# в таблице Users, в противном случае False. Для получения записей используйте SQL запрос.
def is_included(username):
    connection2 = sqlite3.connect("users.db")
    cursor2 = connection2.cursor()
    check_user = cursor2.execute("SELECT * FROM Users WHERE username=?", (username,))
    if check_user.fetchone() is None:
        return False
    else:
        return True


initiate_db()

