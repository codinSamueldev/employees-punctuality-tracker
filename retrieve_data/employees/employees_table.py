from db.sqlite_connection import con, cursor

cursor.execute("SELECT * FROM employees;")
res = cursor.fetchall()

print(res)

con.close()
