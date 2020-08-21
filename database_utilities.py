import sqlite3 as lite


def create_database(database_path: str):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute("drop table if exists userInfo")
        ddl = "create table loginInfo(userName string not null constraint loginInfo_pk primary key,Password string not null);"
        cur.execute(ddl)
        ddl = "create unique index loginInfo_User_Name_uindex on loginInfo(userName);"
        cur.execute(ddl)
    conn.close()


def signUp(database_path: str, userName: str, Password: str):
    conn = lite.connect(database_path)
    cur = conn.cursor()
    cur.execute("INSERT INTO loginInfo(userName, Password) VALUES (?,?)", (userName, Password))


def LogIn(database_path: str, userName: str, Password: str):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        # check to see if the user is in there
        sql = "select count(userName) from loginInfo where userName='" + userName + "'"
        cur.execute(sql)
        count = cur.fetchone()[0]
        if count > 0:
            pass
        else:
            print("User doesn't exist!")


