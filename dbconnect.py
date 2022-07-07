import mysql.connector


def get_balance(chat_id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='telegram_base',
                                             user='root',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select * from users where chat_id = %s", (chat_id,))
            row = cursor.fetchone()
            if row is None:
                return 0
            else:
                return row[1]
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")


    db.execute("SELECT * FROM accounts WHERE telegram_id = %s", (chat_id,))
    if db.rowcount == 0:
        db.execute("INSERT INTO accounts (telegram_id) VALUES (%s)", (chat_id))
        mydb.commit()
        return 0
    else:
        db.execute("SELECT balance FROM accounts WHERE telegram_id = %s", (chat_id,))
        balance = db.fetchone()[0]
        return balance
