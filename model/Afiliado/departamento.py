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

class departamento:

    @staticmethod
    def mostrarDepartamentos():
        try:
            # Consulta para obtener los datos de la tabla de departamentos
            query = "SELECT ID_DEPARTAMENTO, NOMBRE FROM departamento"
            cursor.execute(query)

            # Itera sobre los resultados y muestra cada fila
            for row in cursor:
                print("ID Departamento:", row[0], "Nombre:", row[1])
        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def buscarDepartamento(id_departamento):
        query = "SELECT id_departamento, nombre FROM departamento WHERE id_departamento = :id_departamento"
        try:
            # Supongamos que tienes una conexión configurada como `conn`
            with connection.cursor() as cursor:
                cursor.execute(query, {"id_departamento": id_departamento})
                resultado = cursor.fetchone()

                if resultado:
                    # Devuelve el departamento encontrado
                    print(f"Departamento encontrado: ID = {resultado[0]}, Nombre = {resultado[1]}")
                    return {"id_departamento": resultado[0], "nombre": resultado[1]}
                else:
                    print("No se encontró ningún departamento con el ID proporcionado.")
                    return None
        except oracledb.DatabaseError as e:
            error, = e.args
            print("Error al buscar el departamento:", error.message)
            return None

    buscarDepartamento(1)
    mostrarDepartamentos()