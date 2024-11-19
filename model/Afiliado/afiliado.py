import oracledb
from tkinter import messagebox
# Configura los parámetros de conexión
host = "localhost"
port = 1521
sid = "xe"
user = "LANTHA"
password = "eldenring"

dsn = f"{host}:{port}/{sid}"


oracledb.init_oracle_client(lib_dir="C:/Users/migue/Desktop/instantclient_23_6")

connection = oracledb.connect(user=user, password=password, dsn=dsn)

cursor = connection.cursor()


class afiliado:


    @staticmethod
    def crearAfiliado(id_promotor, nombre, apellido, email, telefono):
        # Variable para almacenar el ID generado
        afiliado_id = cursor.var(int)

        query = """
        INSERT INTO afiliado (id_rango, id_promotor, nombre, apellido, email, fecha_afiliacion, telefono, activo)
        VALUES (:id_rango, :id_promotor, :nombre, :apellido, :email, SYSDATE, :telefono, :activo)
        RETURNING id_afiliado INTO :afiliado_id
        """

        valores = {
            'id_rango': 1,
            'id_promotor': id_promotor,
            'nombre': nombre,
            'apellido': apellido,
            'email': email,
            'telefono': telefono,
            'activo': 1,
            'afiliado_id': afiliado_id  # Vinculamos la variable al parámetro RETURNING
        }

        # Ejecuta la consulta de inserción con los valores proporcionados
        cursor.execute(query, valores)

        # Obtener el ID del afiliado insertado
        afiliado_id_value = int(afiliado_id.getvalue()[0])  # Convertir explícitamente a entero
        cursor.callproc("crear_usuario_afiliado", [afiliado_id_value])

        # Realiza el commit para guardar los cambios
        connection.commit()

    @staticmethod
    def mostrarAfiliados():
        # Consulta para obtener los datos de la tabla
        query = "SELECT id_afiliado, id_rango, id_promotor, nombre, apellido, email, fecha_afiliacion, telefono, activo FROM afiliado"
        cursor.execute(query)

        # Itera sobre los resultados y muestra cada fila
        for row in cursor:
            print("ID Afiliado:", row[0],
                  "ID Rango:", row[1],
                  "ID Promotor:", row[2],
                  "Nombre:", row[3],
                  "Apellido:", row[4],
                  "Email:", row[5],
                  "Fecha de Afiliación:", row[6],
                  "Teléfono:", row[7],
                  "Activo:", row[8])

    @staticmethod
    def actualizarAfiliado(id_afiliado, email_nuevo, telefono_nuevo):
        query = """
        UPDATE afiliado
        SET email = :email_nuevo, telefono = :telefono_nuevo
        WHERE id_afiliado = :id_afiliado
        """

        valores = {
            'id_afiliado': id_afiliado,
            'email_nuevo': email_nuevo,
            'telefono_nuevo': telefono_nuevo
        }

        # Ejecuta la consulta de actualización con los valores proporcionados
        cursor.execute(query, valores)

        # Realiza el commit para guardar los cambios
        connection.commit()

    @staticmethod
    def eliminarAfiliado(id_afiliado):
        query = "DELETE FROM afiliado WHERE id_afiliado = :id_afiliado"

        valores = {
            'id_afiliado': id_afiliado
        }

        # Ejecuta la consulta de eliminación con los valores proporcionados
        cursor.execute(query, valores)

        # Realiza el commit para guardar los cambios
        connection.commit()

    @staticmethod
    def buscarAfiliado(id_afiliado):
        try:
            sql = """
                SELECT id_afiliado, id_rango, id_promotor, nombre, apellido, email, fecha_afiliacion, telefono, activo
                FROM afiliado
                WHERE id_afiliado = :id_afiliado
            """
            valores = (id_afiliado,)

            cursor.execute(sql, valores)
            registro = cursor.fetchone()

            if registro:
                print("Afiliado encontrado:", registro)
                return registro
            else:
                print(f"No se encontró un afiliado con id_afiliado = {id_afiliado}")
                return None

        except oracledb.DatabaseError as error:
            print("Error al buscar afiliado:", error)
            return None


    @staticmethod
    def mostrarAfiliadosPromotor(id_promotor):
        query = """
                   SELECT ID_AFILIADO, NOMBRE, APELLIDO, EMAIL, TELEFONO, FECHA_AFILIACION, ID_RANGO, ACTIVO
                   FROM NEXUS.AFILIADO
                   WHERE ID_PROMOTOR = :id_promotor AND ACTIVO = 1
                   """
        cursor.execute(query, {'id_promotor': id_promotor})

        afiliados = []
        for row in cursor:
            # Solo seleccionamos las columnas necesarias para el Treeview
            afiliados.append((row[0], row[1], row[6]))  # ID, Nombre y Rango

        return afiliados

    @staticmethod
    def mostrarVentasAfiliado(id_promotor):
        query = """
                select fv.id_factura_venta, sum(dv.precio_unitario*dv.cantidad)
                from afiliado a
                join factura_venta fv on a.id_afiliado = fv.id_afiliado
                join detalle_venta dv on fv.id_factura_Venta = dv.id_factura_Venta
                group by (fv.id_factura_venta)
                   """
        cursor.execute(query, {'id_promotor': id_promotor})

        afiliados = []
        for row in cursor:
            # Solo seleccionamos las columnas necesarias para el Treeview
            afiliados.append((row[0], row[1], row[6]))  # ID, Nombre y Rango

        return afiliados
    @staticmethod
    def obtener_nombre_rango(id_rango):
        sql = """
        SELECT nombre
        FROM rango
        WHERE id_rango = :1
        """
        cursor.execute(sql, (id_rango,))
        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]
        else:
            return "Rango no encontrado"

class Sesion:
    def __init__(self, id_afiliado, id_rango, id_promotor, nombre, apellido,
                 email, fecha_afiliacion, telefono, activo):
        self.id_afiliado = id_afiliado
        self.id_rango = id_rango
        self.id_promotor = id_promotor
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.fecha_afiliacion = fecha_afiliacion
        self.telefono = telefono
        self.activo = activo

