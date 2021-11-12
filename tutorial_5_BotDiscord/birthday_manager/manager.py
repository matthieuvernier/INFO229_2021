import mysql.connector
import os, time
import create_database

#######################
print("start birthday manager...")
create_database.main()

DATABASE = "bot"

DATABASE_IP = str(os.environ['DATABASE_IP'])

DATABASE_USER = "root"
DATABASE_USER_PASSWORD = "root"
DATABASE_PORT=3306

not_connected = True

while(not_connected):
	try:
		print(DATABASE_IP,"IP")
		db_connection = mysql.connector.connect(user=DATABASE_USER,host=DATABASE_IP,port=DATABASE_PORT, password=DATABASE_USER_PASSWORD)
		not_connected = False

	except Exception as e:
		time.sleep(3)
		print(e, "error!!!")
		print("can't connect to mysql server, might be intializing")
		
cursor = db_connection.cursor()
cursor.execute(f"USE {DATABASE}")

while(True):
    cursor.execute('''SELECT member,date FROM birthday;''')

    for (member, date) in cursor:
        print("{} nació el {:%d %b %Y}".format(member,date))

    time.sleep(5*60)