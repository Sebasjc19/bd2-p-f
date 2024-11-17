import oracledb

host = "localhost"
port = 1521
sid = "xe"
user = "nexus"
password = "admin1234"

dsn = f"{host}:{port}/{sid}"

oracledb.init_oracle_client()
connection = oracledb.connect(user=user, password=password, dsn=dsn)
cursor = connection.cursor()

class transportadora:

    @staticmethod
    def insertarTransportadora(id_transportadora, nombre):
        try:
            sql = """
                INSERT INTO Transportadora (id_transportadora, nombre)
                VALUES (:1, :2)
            """
            valores = (id_transportadora, nombre)
            cursor.execute(sql, valores)

            # Confirmar los cambios
            connection.commit()
            print(cursor.rowcount, "registro(s) ingresado(s) con éxito")

        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def eliminarTransportadora(id_transportadora):
        try:
            sql = "DELETE FROM Transportadora WHERE id_transportadora = :1"
            valores = (id_transportadora,)
            cursor.execute(sql, valores)

            # Confirmar los cambios
            connection.commit()
            print(cursor.rowcount, "registro(s) eliminado(s) con éxito")

        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def actualizarTransportadora(id_transportadora, nombre):
        try:
            sql = """
                UPDATE Transportadora
                SET nombre = :2
                WHERE id_transportadora = :1
            """
            valores = (id_transportadora, nombre)
            cursor.execute(sql, valores)

            # Confirmar los cambios
            connection.commit()
            print(cursor.rowcount, "registro(s) actualizado(s) con éxito")

        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def buscarTransportadora(id_transportadora):
        try:
            sql = """
                SELECT id_transportadora, nombre
                FROM Transportadora
                WHERE id_transportadora = :1
            """
            valores = (id_transportadora,)
            cursor.execute(sql, valores)

            # Obtener el resultado de la consulta
            registro = cursor.fetchone()

            if registro:
                print("Registro encontrado:", registro)
                return registro
            else:
                print("No se encontró un registro con id_transportadora =", id_transportadora)
                return None

        finally:

            if cursor:
                cursor.close()
            if connection:
                connection.close()


