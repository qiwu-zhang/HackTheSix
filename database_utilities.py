import sqlite3 as lite


def create_database(database_path: str):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute("drop table if exists userInfo")
        ddl = "create table userInfo(userName str not null,Password str not null);"
        cur.execute(ddl)
    conn.close()


def insert_User(database_path: str, userName: str, Password: str):
    conn = lite.connect(database_path)
    cur = conn.cursor()
    cur.execute("insert into userInfo(userName, Password) values (?,?)", (userName, Password))
    conn.commit()
    conn.close()

def login(database_path:str, userName: str, Password: str):
    conn = lite.connect(database_path)
    cur = conn.cursor()
    try:
        userName_collection = cur.execute("select userName from userInfo")
        for row in userName_collection:
            if (userName in row):
                print("%s" %userName)
                pw = cur.execute("select Password from userInfo WHERE userName = ?", (userName,))
                if (Password in pw):
                    print("login successful")
                    return 1
        print("Username is incorrect")
    except IOError:
        print("something's wrong")

    print("login successful")