import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="people",
    user="mariaseal",
    password="password",
    autocommit=True
)

def gatemployeesbylastname(last_name):
    sql = "select id, lastname, firstname, salary from employees"
    sql += " where lastname='" + last_name + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
    return




