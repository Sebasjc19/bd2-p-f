import oracledb

# Configura los parámetros de conexión
host = "localhost"
port = 1521
sid = "xe"
user = "nexus"
password = "admin1234"

# Establece el DSN (Data Source Name) para la conexión
dsn = f"{host}:{port}/{sid}"

# se establece una conexión directa
oracledb.init_oracle_client()

# Conectar a la base de datos
connection = oracledb.connect(user=user, password=password, dsn=dsn)

# Imprimir la versión de la base de datos
print("Versión de la base de datos:", connection.version)

# Cierra la conexión
connection.close()
