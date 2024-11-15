import tkinter as tk
from tkinter import messagebox
import oracledb

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

    # se establece una conexión directa
    oracledb.init_oracle_client()
    try:
        # Intenta conectarte a la base de datos
        connection = oracledb.connect(user=user, password=password, dsn=dsn)
        # Si la conexión es exitosa
        messagebox.showinfo("Autenticación exitosa", "Conexión exitosa a la base de datos")
        connection.close()
    except oracledb.DatabaseError as e:
        # Si la conexión falla, muestra un mensaje de error
        messagebox.showerror("Error de autenticación", "Nombre de usuario o contraseña incorrectos")


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
