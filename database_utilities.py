import sqlite3 as lite


def create_database(database_path: str):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute("drop table if exists userInfo")
        ddl = "create table userInfo(userName str not null,Password str not null,age int default 18 not null,city text default Toronto not null,monthly_income int default 4000 not null, yearly_income int default 10000 not null,saving_goaly_yearly int default 5000,saving_plan_1 text default unknown not null,saving_plan_2 text default unknown not null,saving_plan_3 text default unknown not null);"
        cur.execute(ddl)
    conn.close()


def insert_User(database_path: str, userName: str, Password: str):
    conn = lite.connect(database_path)
    cur = conn.cursor()
    cur.execute("insert into userInfo(userName, Password) values (?,?)", (userName, Password))
    conn.commit()
    conn.close()


def login(database_path: str, userName: str, Password: str):
    conn = lite.connect(database_path)
    cur = conn.cursor()
    try:
        cur.execute("select userName from userInfo")
        userName_collection = cur.fetchall()

        for row in userName_collection:
            if userName in row:
                cur.execute("select Password from userInfo WHERE userName = ?", (userName,))
                pw = cur.fetchall()
                for col in pw:
                    if Password in col:
                        print("login successful")
                        conn.commit()
                        conn.close()
                        return 1
                    else:
                        print("password isn't correct")
            else:
                print("Username does not exist")

    except IOError as e:
        print(e)
    conn.commit()
    conn.close()
    return 0


def update_profile(database_path: str, userName: str, age: int, city: str, monthly_income:int, yearly_income:int,saving_goal:int):
    conn = lite.connect(database_path)
    cur = conn.cursor()
    cur.execute('''UPDATE userInfo SET age = ? WHERE userName = ?''', (age, userName))
    cur.execute('''UPDATE userInfo SET city = ? WHERE userName = ?''', (city, userName))
    cur.execute('''UPDATE userInfo SET monthly_income = ? WHERE userName = ?''', (monthly_income, userName))
    cur.execute('''UPDATE userInfo SET yearly_income = ? WHERE userName = ?''', (yearly_income, userName))
    cur.execute('''UPDATE userInfo SET saving_goal = ? WHERE userName = ?''', (saving_goal, userName))
    conn.commit()
    conn.close()



