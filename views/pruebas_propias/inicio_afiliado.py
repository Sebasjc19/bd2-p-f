import tkinter as tk
from tkinter import ttk
import inicio_productos  # Importa el archivo donde está la clase de la ventana de productos

# Clase para la ventana principal
class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Información de Usuario")

        # Etiquetas para mostrar información
        self.label_nombre = tk.Label(root, text="Nombre: Juan Pérez")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_email = tk.Label(root, text="Email: juanperez@example.com")
        self.label_email.grid(row=1, column=0, padx=10, pady=10)

        self.label_rango = tk.Label(root, text="Rango: Afiliado Nivel 1")
        self.label_rango.grid(row=2, column=0, padx=10, pady=10)

        # Botones para las opciones de usuario
        self.btn_ver_productos = tk.Button(root, text="Ver Productos", command=self.abrir_ventana_productos)
        self.btn_ver_productos.grid(row=0, column=1, padx=20, pady=10)

        self.btn_ver_ventas = tk.Button(root, text="Ver Ventas", command=self.ver_ventas)
        self.btn_ver_ventas.grid(row=1, column=1, padx=20, pady=10)

        self.btn_ver_afiliados = tk.Button(root, text="Ver Afiliados de mi Red", command=self.ver_afiliados)
        self.btn_ver_afiliados.grid(row=2, column=1, padx=20, pady=10)

    # Función para abrir la ventana de productos
    def abrir_ventana_productos(self):
        ventana_productos = inicio_productos.VentanaProductos(self.root)

    # Funciones para los otros botones
    def ver_ventas(self):
        print("Ver ventas")

    def ver_afiliados(self):
        print("Ver afiliados de mi red")

    def ver_despachos(self):
        print("Ver despachos")

# Crear la ventana principal
root = tk.Tk()
app = VentanaPrincipal(root)

# Ejecutar la aplicación
root.mainloop()
