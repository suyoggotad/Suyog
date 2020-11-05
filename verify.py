import mysql.connector as sql
mydb = sql.connect(
        host="localhost",
        user="root",
        password="!SyG!216")
mycursor = mydb.cursor()

def verify_data_table(in_db):
    mycursor.execute("show databases")
    db_list = mycursor.fetchall()
    flag = 0
    for i in range(0, len(db_list)):
        if db_list[i][0] == in_db:
            flag = 1
    if flag==1:
        return True

    else:
        return False
