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

class departamento:
    @staticmethod
    def crearDepartamento(nombre):
        try:
            query = """
                INSERT INTO departamento (nombre)
                VALUES (:nombre)
                """

            valores = {
                'nombre': nombre
            }

            # Ejecuta la consulta de inserción con los valores proporcionados
            cursor.execute(query, valores)

            # Realiza el commit para guardar los cambios
            connection.commit()

            print(f"Departamento '{nombre}' creado exitosamente.")
        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

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
    def actualizarDepartamento(id_departamento, nombre_nuevo):
        query = """
        UPDATE departamento
        SET nombre = :nombre_nuevo
        WHERE id_departamento = :id_departamento
        """

        valores = {
            'id_departamento': id_departamento,
            'nombre_nuevo': nombre_nuevo
        }

        # Ejecuta la consulta de actualización con los valores proporcionados
        cursor.execute(query, valores)

        # Realiza el commit para guardar los cambios
        connection.commit()

        print(f"Departamento con ID {id_departamento} actualizado a '{nombre_nuevo}'.")

    @staticmethod
    def eliminarDepartamento(id_departamento):
        # Consulta para eliminar un departamento por su ID
        query = "DELETE FROM departamento WHERE ID_DEPARTAMENTO = :id"

        # Ejecuta la consulta con el parámetro
        cursor.execute(query, {"id": id_departamento})

        # Confirma los cambios en la base de datos
        connection.commit()

        print(f"Departamento con ID {id_departamento} ha sido eliminado.")

    @staticmethod
    def buscarDepartamento(id_departamento):
        try:
            sql = """
                SELECT id_departamento, nombre
                FROM departamento
                WHERE id_departamento = :1
            """
            valores = (id_departamento,)
            cursor.execute(sql, valores)

            # Obtener el resultado de la consulta
            registro = cursor.fetchone()

            if registro:
                print("Registro encontrado:", registro)
                return registro
            else:
                print(f"No se encontró un registro con id_departamento = {id_departamento}")
                return None

        except Exception as e:
            print(f"Error al buscar el departamento: {e}")
            return None

        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    mostrarDepartamentos()
    buscarDepartamento(3)

