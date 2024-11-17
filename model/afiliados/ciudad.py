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

class ciudad:

    @staticmethod
    def crearCiudad(id_departamento, nombre):
        try:
            query = """
            INSERT INTO ciudad (id_departamento, nombre)
            VALUES (:id_departamento, :nombre)
            """

            valores = {
                'id_departamento': id_departamento,
                'nombre': nombre
            }

            # Ejecuta la consulta de inserción con los valores proporcionados
            cursor.execute(query, valores)

            # Realiza el commit para guardar los cambios
            connection.commit()

        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def mostrarCiudades():
        try:
            # Consulta para obtener los datos de la tabla Ciudades
            query = "SELECT id_ciudad, id_departamento, nombre FROM ciudad"
            cursor.execute(query)

            # Itera sobre los resultados y muestra cada fila
            for row in cursor:
                print("ID Ciudad:", row[0],
                      "ID Departamento:", row[1],
                      "Nombre:", row[2])
        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def actualizarCiudad(id_ciudad, nombre_nuevo, id_departamento_nuevo):
        try:
            query = """
            UPDATE ciudad
            SET nombre = :nombre_nuevo, id_departamento = :id_departamento_nuevo
            WHERE id_ciudad = :id_ciudad
            """

            valores = {
                'id_ciudad': id_ciudad,
                'nombre_nuevo': nombre_nuevo,
                'id_departamento_nuevo': id_departamento_nuevo
            }

            # Ejecuta la consulta de actualización con los valores proporcionados
            cursor.execute(query, valores)

            # Realiza el commit para guardar los cambios
            connection.commit()
        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def eliminarCiudad(id_ciudad):
        try:
            query = "DELETE FROM ciudad WHERE id_ciudad = :id_ciudad"

            valores = {
                'id_ciudad': id_ciudad
            }

            # Ejecuta la consulta de eliminación con los valores proporcionados
            cursor.execute(query, valores)

            # Realiza el commit para guardar los cambios
            connection.commit()
        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def buscarCiudad(id_ciudad):
        try:
            # Crear un nuevo cursor para la consulta
            cursor = connection.cursor()

            # Consulta SQL para buscar la ciudad por ID
            sql = """
                SELECT id_ciudad, id_departamento, nombre
                FROM ciudad
                WHERE id_ciudad = :1
            """
            valores = (id_ciudad,)
            cursor.execute(sql, valores)

            # Obtener el resultado de la consulta
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
            # Cerrar el cursor
            cursor.close()

    # mostrarCiudades()
