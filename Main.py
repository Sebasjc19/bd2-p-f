import oracledb

# Configura los parámetros de conexión
host = "localhost"
port = 1521
sid = "xe"
user = "nexus"
password = "admin1234"

# Define el DSN
dsn = f"{host}:{port}/{sid}"

# se establece una conexión directa
oracledb.init_oracle_client()
# Conéctate a la base de datos
connection = oracledb.connect(user=user, password=password, dsn=dsn)

# Crea un cursor para ejecutar la consulta
cursor = connection.cursor()

# Ejecuta una consulta sencilla
query = "SELECT id_afiliado, nombre FROM afiliado"
cursor.execute(query)

# Itera sobre los resultados y muestra cada fila
for row in cursor:
    print("ID:", row[0], "Nombre:", row[1])

# Cierra el cursor y la conexión
cursor.close()
connection.close()
