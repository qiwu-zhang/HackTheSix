import os
import sqlite3 as lite
from sqlite3 import IntegrityError


def make_connection():
    global conn
    global cur
    os.chdir(os.path.dirname(__file__))
    path = os.path.join(os.getcwd(), "LoginInfo.db")
    conn = lite.connect(path)
    cur = conn.cursor()
    print(conn)
    print(cur)


def create_table():
    cur.execute("drop table if exists userInfo")
    ddl = "create table userInfo(userName str not null,Password str not null,age int default 18 not null,city text default Toronto not null,monthly_income int default 4000 not null, yearly_income int default 10000 not null,saving_goaly_yearly int default 5000,saving_plan_1 text default unknown not null,saving_plan_2 text default unknown not null,saving_plan_3 text default unknown not null);"
    cur.execute(ddl)


def create_table_saving_plans():
    cur.execute("drop table if exists savingPlans")
    ddl = "create table savingPlans(name text not null,type text not null,rate integer default 2 constraint savingPlans_pk primary key autoincrement);"
    cur.execute(ddl)


def insert_User(userName: str, Password: str):
    try:
        cur.execute("insert into userInfo(userName, Password) values (?,?)", (userName, Password))
    except IntegrityError as e:
        print("Duplicate user")

    conn.commit()

def insert_saving_plans(name:str,type:str):
    cur.execute("insert into savingPlans(name, type) values (?,?)", (name, type))


def login(userName: str, Password: str):
    try:
        cur.execute("select userName, Password from userInfo where userName = ?",
                    (userName,))  ## Select only username that you care about
        results = cur.fetchall()
        if len(results) == 0:
            return 0

        if (userName, Password) == (results[0][0], str(results[0][1])):
            print("login successful")
            return 1
    except IOError as e:
        print(e)

    return 0


def update_profile(userName: str, age: int, city: str, monthly_income: int, yearly_income: int, saving_goal: int):
    cur.execute('''UPDATE userInfo SET age = ? WHERE userName = ?''', (age, userName))
    cur.execute('''UPDATE userInfo SET city = ? WHERE userName = ?''', (city, userName))
    cur.execute('''UPDATE userInfo SET monthly_income = ? WHERE userName = ?''', (monthly_income, userName))
    cur.execute('''UPDATE userInfo SET yearly_income = ? WHERE userName = ?''', (yearly_income, userName))
    cur.execute('''UPDATE userInfo SET saving_goal = ? WHERE userName = ?''', (saving_goal, userName))
    conn.commit()


def close():
    conn.close()
