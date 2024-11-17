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


class factura_venta:

    @staticmethod
    def insertarfactura_venta(id_factura_venta, id_estadoventa, id_afiliado, fecha):
        try:
            cursor = connection.cursor()

            sql = """
                INSERT INTO Factura_Venta (id_factura_venta, id_estadoventa, id_afiliado, fecha)
                VALUES (:1, :2, :3, :4)
            """
            valores = (id_factura_venta, id_estadoventa, id_afiliado, fecha)
            cursor.execute(sql, valores)

            # Confirmar los cambios
            connection.commit()
            print(cursor.rowcount, "registro(s) ingresado(s) con éxito")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def eliminarfactura_venta(id_factura_venta):
        try:
            cursor = connection.cursor()

            sql = "DELETE FROM Factura_Venta WHERE id_factura_venta = :1"
            valores = (id_factura_venta,)
            cursor.execute(sql, valores)

            # Confirmar los cambios
            connection.commit()
            print(cursor.rowcount, "registro(s) eliminado(s) con éxito")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def eliminarfactura_venta(id_factura_venta):
        try:
            sql = "DELETE FROM Factura_Venta WHERE id_factura_venta = :1"
            valores = (id_factura_venta,)
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
    def buscarfactura_venta(id_factura_venta):
        try:
            sql = """
                SELECT id_factura_venta, id_estadoventa, id_afiliado, fecha
                FROM Factura_Venta
                WHERE id_factura_venta = :1
            """
            valores = (id_factura_venta,)
            cursor.execute(sql, valores)

            # Obtener el resultado de la consulta
            registro = cursor.fetchone()

            if registro:
                print("Registro encontrado:", registro)
                return registro
            else:
                print("No se encontró un registro con id_factura_venta =", id_factura_venta)
                return None

        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()




