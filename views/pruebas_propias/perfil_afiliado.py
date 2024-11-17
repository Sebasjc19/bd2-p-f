import tkinter as tk
from tkinter import ttk

from views.pruebas_conexiones.afiliados_red import VentanaAfiliados


# Clase para la ventana principal
class VentanaPrincipal:
    def __init__(self, root, sesion):
        self.root = root
        self.sesion = sesion  # Guardamos el objeto sesión
        self.root.title("Información de Usuario")

        # Crear las etiquetas para mostrar la información del afiliado
        self.label_id_afiliado = tk.Label(root, text=f"ID Afiliado: {self.sesion.id_afiliado}")
        self.label_id_afiliado.grid(row=0, column=0, padx=10, pady=10)

        self.label_rango = tk.Label(root, text=f"Rango: {self.sesion.id_rango}")
        self.label_rango.grid(row=1, column=0, padx=10, pady=10)

        self.label_promotor = tk.Label(root, text=f"Promotor: {self.sesion.id_promotor}")
        self.label_promotor.grid(row=2, column=0, padx=10, pady=10)

        self.label_nombre = tk.Label(root, text=f"Nombre: {self.sesion.nombre} {self.sesion.apellido}")
        self.label_nombre.grid(row=3, column=0, padx=10, pady=10)

        self.label_email = tk.Label(root, text=f"Email: {self.sesion.email}")
        self.label_email.grid(row=4, column=0, padx=10, pady=10)

        self.label_fecha_afiliacion = tk.Label(root, text=f"Fecha de Afiliación: {self.sesion.fecha_afiliacion}")
        self.label_fecha_afiliacion.grid(row=5, column=0, padx=10, pady=10)

        self.label_telefono = tk.Label(root, text=f"Teléfono: {self.sesion.telefono}")
        self.label_telefono.grid(row=6, column=0, padx=10, pady=10)

        self.label_activo = tk.Label(root, text=f"Activo: {'Sí' if self.sesion.activo else 'No'}")
        self.label_activo.grid(row=7, column=0, padx=10, pady=10)

        # Botón para ver ventas
        self.boton_ventas = tk.Button(root, text="Ver Ventas", command=self.ver_ventas)
        self.boton_ventas.grid(row=8, column=0, padx=10, pady=10)

        # Botón para ver afiliados
        self.boton_afiliados = tk.Button(root, text="Ver Afiliados", command=self.ver_afiliados)
        self.boton_afiliados.grid(row=9, column=0, padx=10, pady=10)

        # Botón para ver despachos
        self.boton_despachos = tk.Button(root, text="Ver Despachos", command=self.ver_despachos)
        self.boton_despachos.grid(row=10, column=0, padx=10, pady=10)

    # Función para abrir la ventana de productos

    # Funciones para los otros botones
    def ver_ventas(self):
        print("Ver ventas")

    def ver_afiliados(self):
        # Crear una nueva ventana de afiliados cuando se hace clic en el botón
        ventana_afiliados = tk.Toplevel(self.root)
        VentanaAfiliados(ventana_afiliados, self.sesion)  # Abrir la ventana de afiliados

    def ver_despachos(self):
        print("Ver despachos")


# Configuración de la ventana de login
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
boton_login = tk.Button(root, text="Iniciar sesión")
boton_login.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
