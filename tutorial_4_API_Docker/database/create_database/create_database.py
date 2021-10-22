import mysql.connector
import os, time

def create_database(db_connection,db_name,cursor):
	cursor.execute(f"CREATE DATABASE {db_name};")
	cursor.execute(f"COMMIT;")
	cursor.execute(f"USE {db_name};")
	
	# Tabla news
	cursor.execute('''CREATE TABLE news (
		id_news INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
		url TEXT,
		title TEXT, 
		date DATE,
		media_outlet VARCHAR(50),
		category VARCHAR(100)
        );''')

	cursor.execute("SET GLOBAL time_zone = 'UTC';")
	cursor.execute("SET SESSION time_zone = 'UTC';")

	cursor.execute("COMMIT;") 

def insert_data(cursor):
    print("insert")
    cursor.execute('''INSERT INTO news (url,title,date,media_outlet,category) VALUES
    ('https://www.biobiochile.cl/noticias/futbol-internacional/chilenos-en-el-exterior/2021/10/21/carlos-palacios-ingreso-en-el-segundo-tiempo-en-empate-de-inter-ante-bragantino.shtml
','Carlos Palacios ingresó en el segundo tiempo en empate de Inter ante Bragantino 
','2021-10-21','biobiochile','deportes'),
    ('https://www.biobiochile.cl/noticias/economia/actualidad-economica/2021/10/20/por-sexta-semana-consecutiva-suben-todas-las-bencinas-en-63-pesos-por-litros.shtml
','Por sexta semana consecutiva suben todas las bencinas en 6,3 pesos por litro
','2021-10-20','biobiochile','economia'),
    ('https://www.biobiochile.cl/biobiotv/programas/podria-ser-peor/2021/10/21/vicepdte-colegio-medico-si-aumenta-rapido-la-demanda-covid-19-no-alcanzaremos-a-responder.shtml
','Vicepdte. Colegio Médico: "Si aumenta rápido la demanda Covid-19, no alcanzaremos a responder"
','2021-10-21','biobiochile','salud');
    ''')
    cursor.execute("COMMIT;") 

#######################
DATABASE = "tutorial_4"

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

try:
	cursor.execute(f"USE {DATABASE}")
	print(f"Database: {DATABASE} already exists")
except Exception as e:
    create_database(db_connection,DATABASE,cursor)
    insert_data(cursor)
    print(f"Succesfully created: {DATABASE}")
