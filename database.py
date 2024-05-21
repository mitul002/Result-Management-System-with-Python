import sqlite3

def create_database():
    connect = sqlite3.connect(database="rms.db")
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS course (
                            cid INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            duration INTEGER,
                            charges INTEGER,
                            description TEXT
                        )''')
    connect.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS student (
                            roll INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            email TEXT,
                            gender TEXT,
                            birthday TEXT,
                            contact TEXT,
                            course TEXT,
                            city TEXT,
                            address TEXT
                        )''')


    cursor.execute('''CREATE TABLE IF NOT EXISTS result (
                                roll INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                course TEXT,
                                marks TEXT,
                                full_marks TEXT,
                                percent TEXT
                            )''')

    connect.commit()
    print("Database and tables created successfully.")

if __name__ == "__main__":
    create_database()

