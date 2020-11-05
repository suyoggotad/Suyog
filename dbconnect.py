import mysql.connector as sql
import verify

db=sql.connect(
    host='localhost',
    user='root',
    password='!SyG!216')

mycursor=db.cursor()

def create_tables():
    db_name='tax_profile'
    Personal='personal_info'
    Address='addresss'
    Bank='bank_info'
    Income='income_details'

    perform=verify.verify_data_table(db_name)

    if perform== False:
        mycursor.execute(f'create database {db_name}')
        print('db create')
        mycursor.execute(f'use {db_name}')
        mycursor.execute(f'create table {Personal} (client_id int not null auto_increment, name varchar(30), pan varchar(20),gender varchar(10), primary key(client_id))')
        mycursor.execute(f'create table {Address} (client_id int not null auto_increment, address varchar(255), primary key(client_id))')
        mycursor.execute(f'create table {Income} (client_id int not null auto_increment,Year varchar(10), Total_income varchar(30) , Net_income varchar(30), Total_tax varchar(30), primary key(client_id))')
        mycursor.execute(f'create table {Bank} (client_id int not null auto_increment, Account_Number varchar(30),IFSC_Code varchar(30), Branch varchar(30), primary key(client_id) )')
        print('table created')
    else:
        print('table already exits')

def insert_data(add, query):
    mycursor.execute(f'use tax_profile')
    mycursor.execute(add, query)
    db.commit()

def search_in_table(disp_sql):
    mycursor.execute("USE tax_profile")
    mycursor.execute(disp_sql)      
    row = mycursor.fetchone()
    if row is not None:
        return row
    else:
        return False

def view_all(disp_sql):
    mycursor.execute("USE tax_profile")
    mycursor.execute(disp_sql)      
    row = mycursor.fetchall()
    if row is not None:
        return row
    else:
        return False