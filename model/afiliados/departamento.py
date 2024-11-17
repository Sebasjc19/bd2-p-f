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


# Para crear un departamento
def crearDepartamento(nombre):
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


def mostrarDepartamentos():
    # Consulta para obtener los datos de la tabla de departamentos
    query = "SELECT ID_DEPARTAMENTO, NOMBRE FROM departamento"
    cursor.execute(query)

    # Itera sobre los resultados y muestra cada fila
    for row in cursor:
        print("ID Departamento:", row[0], "Nombre:", row[1])


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


def eliminarDepartamento(id_departamento):
    # Consulta para eliminar un departamento por su ID
    query = "DELETE FROM departamento WHERE ID_DEPARTAMENTO = :id"

    # Ejecuta la consulta con el parámetro
    cursor.execute(query, {"id": id_departamento})

    # Confirma los cambios en la base de datos
    connection.commit()

    print(f"Departamento con ID {id_departamento} ha sido eliminado.")


# Llamada a la función para insertar un nuevo afiliados
# crearAfiliado(1, 1, 'Pablo', 'Alborán', 'dasdfgasdfsa@example.com', '1234567890', 1)
# eliminarAfiliado(64)

# actualizarAfiliado(1, "juanpereza@gmail.com", 3199494949)

# eliminarDepartamento(11)
# actualizarDepartamento(2,"Quindío")
crearDepartamento("Sucre")

# eliminarDepartamento(6)
mostrarDepartamentos()

# Cierra el cursor y la conexión
cursor.close()
connection.close()
