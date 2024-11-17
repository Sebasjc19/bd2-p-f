import tkinter as tk
from tkinter import messagebox
import oracledb
import re
from model.afiliados.afiliado import afiliado
from model.sesion import Sesion
from views.pruebas_propias.perfil_afiliado import VentanaPrincipal

# Configuración de la base de datos (ajusta estos parámetros según tu configuración)
host = "localhost"
port = 1521
sid = "xe"

# Función para autenticarse en la base de datos
def autenticar():
    # Obtén el nombre de usuario y la contraseña de los campos de entrada
    user = entry_usuario.get()
    password = entry_contrasena.get()

    # Configura el DSN
    dsn = f"{host}:{port}/{sid}"

    # Se establece una conexión directa
    oracledb.init_oracle_client()
    try:
        # Intenta conectarte a la base de datos
        connection = oracledb.connect(user=user, password=password, dsn=dsn)
        # Si la conexión es exitosa
        messagebox.showinfo("Autenticación exitosa", "Conexión exitosa a la base de datos")

        id_afiliado = re.sub("Password_", "", password)
        # Obtener el afiliado
        afiliadoEncontrar = afiliado.buscarAfiliado(id_afiliado)

        # Crear la sesión con los datos encontrados
        sesion = Sesion(
            id_afiliado=afiliadoEncontrar[0],
            id_rango=afiliadoEncontrar[1],
            id_promotor=afiliadoEncontrar[2],
            nombre=afiliadoEncontrar[3],
            apellido=afiliadoEncontrar[4],
            email=afiliadoEncontrar[5],
            fecha_afiliacion=afiliadoEncontrar[6],
            telefono=afiliadoEncontrar[7],
            activo=afiliadoEncontrar[8]
        )

        # Llamar a la ventana principal pasando la sesión
        root.destroy()  # Detener el ciclo de eventos de la ventana de login
        mostrar_ventana_principal(sesion)  # Mostrar la ventana principal con la sesión

    except oracledb.DatabaseError as e:
        # Si la conexión falla, muestra un mensaje de error
        messagebox.showerror("Error de autenticación", "Nombre de usuario o contraseña incorrectos")


# Función para mostrar la ventana principal con la sesión
def mostrar_ventana_principal(sesion):
    # Crear la ventana principal, pasando la sesión al constructor
    ventana_principal = tk.Tk()
    VentanaPrincipal(ventana_principal, sesion)  # Pasamos la sesión
    ventana_principal.mainloop()


# Configuración de la ventana de Tkinter
root = tk.Tk()
root.title("Autenticación con Oracle")
root.geometry("300x200")

# Etiquetas y campos de entrada
label_usuario = tk.Label(root, text="Nombre de usuario:")
label_usuario.pack(pady=5)

entry_usuario = tk.Entry(root)
entry_usuario.pack(pady=5)

label_contrasena = tk.Label(root, text="Contraseña:")
label_contrasena.pack(pady=5)

entry_contrasena = tk.Entry(root, show="*")  # Campo de contraseña oculto
entry_contrasena.pack(pady=5)

# Botón para iniciar sesión
boton_login = tk.Button(root, text="Iniciar sesión", command=autenticar)
boton_login.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
