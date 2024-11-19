import oracledb

# Configura los parámetros de conexión
host = "localhost"
port = 1521
sid = "xe"
user = "LANTHA"
password = "eldenring"

# Define el DSN
dsn = f"{host}:{port}/{sid}"

# se establece una conexión directa
oracledb.init_oracle_client(lib_dir="C:/Users/migue/Desktop/instantclient_23_6")
# Conéctate a la base de datos
connection = oracledb.connect(user=user, password=password, dsn=dsn)

# Crea un cursor para ejecutar la consulta
cursor = connection.cursor()

class ciudad:

    @staticmethod
    def mostrarCiudades():
        try:
            query = "SELECT id_ciudad, id_departamento, nombre FROM ciudad"
            cursor.execute(query)

            for row in cursor:
                print("ID Ciudad:", row[0],
                      "ID Departamento:", row[1],
                      "Nombre:", row[2])
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def buscarCiudad(id_ciudad):
        try:
            cursor = connection.cursor()
            sql = """
                SELECT id_ciudad, id_departamento, nombre
                FROM ciudad
                WHERE id_ciudad = :1
            """
            valores = (id_ciudad,)
            cursor.execute(sql, valores)
            registro = cursor.fetchone()

            if registro:
                print("Ciudad encontrada:", registro)
                return registro
            else:
                print(f"No se encontró una ciudad con id_ciudad = {id_ciudad}")
                return None

        except Exception as e:
            print(f"Error al buscar la ciudad: {e}")
            return None

        finally:
            cursor.close()

