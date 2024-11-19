import oracledb

host = "localhost"
port = 1521
sid = "xe"
user = "LANTHA"
password = "eldenring"

dsn = f"{host}:{port}/{sid}"

oracledb.init_oracle_client()
connection = oracledb.connect(user=user, password=password, dsn=dsn)
cursor = connection.cursor()


class factura_venta:

    @staticmethod
    def insertar_factura_venta(id_factura_venta, id_estadoventa, id_afiliado, fecha):
        query = """
            INSERT INTO Factura_Venta (id_factura_venta, id_estadoventa, id_afiliado, fecha)
            VALUES (:id_factura_venta, :id_estadoventa, :id_afiliado, :fecha)
        """
        valores = {
            "id_factura_venta": id_factura_venta,
            "id_estadoventa": id_estadoventa,
            "id_afiliado": id_afiliado,
            "fecha": fecha
        }
        try:
            # Supongamos que tienes una conexión configurada como conn
            with connection.cursor() as cursor:
                cursor.execute(query, valores)
                connection.commit()
                print("Factura de venta insertada exitosamente")
        except oracledb.DatabaseError as e:
            error, = e.args
            print("Error al insertar la factura de venta:", error.message)



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



    def mostrar_factura_venta(id_factura_venta):
        query = """
            SELECT id_factura_venta, id_estadoventa, id_afiliado, fecha
            FROM Factura_Venta
            WHERE id_factura_venta = :id_factura_venta
        """
        valores = {"id_factura_venta": id_factura_venta}
        try:
            # Supongamos que tienes una conexión configurada como conn
            with connection.cursor() as cursor:
                cursor.execute(query, valores)
                factura = cursor.fetchone()

                if factura:
                    print("Factura encontrada:", factura)
                    return factura
                else:
                    print(f"No se encontró una factura con id_factura_venta = {id_factura_venta}")
                    return None
        except oracledb.DatabaseError as e:
            error, = e.args
            print("Error al buscar la factura de venta:", error.message)


