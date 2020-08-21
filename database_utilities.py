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
    cur.execute("INSERT INTO userInfo(userName, Password) VALUES (?,?)", (userName, Password))
