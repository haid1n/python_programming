import mysql.connector

try:
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="@n1m34l1f3",
		database="py_db_schema"
		)

	mycursor = mydb.cursor()

	sql = "INSERT INTO customers(name, address) VALUES (%s, %s)"

	values = ("John Doe", "123 Main St")

	mycursor.execute(sql, values)

	mydb.commit()

	print(mycursor.rowcount, "record inserted")

except mysql.connector.Error as err:
	print(f"Error: {err}")

finally:
	if "mycursor" in locals() and mycursor:
		mycursor.close()

	if "mydb" in locals() and mydb:
		mydb.close()