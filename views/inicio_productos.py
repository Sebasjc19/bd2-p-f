import tkinter as tk
from tkinter import messagebox, ttk

# Clase para la ventana de productos
class VentanaProductos:
    def __init__(self, parent):
        self.parent = parent
        # Crear la ventana secundaria
        self.ventana_productos = tk.Toplevel(self.parent)  # Ventana secundaria
        self.ventana_productos.title("Tabla de Productos")

        # Crear un Treeview para mostrar la tabla
        self.tree = ttk.Treeview(self.ventana_productos, columns=("ID Producto", "Nombre Producto", "Cantidad", "Precio Venta", "Precio Compra"), show="headings")

        # Definir las columnas
        self.tree.heading("ID Producto", text="ID Producto")
        self.tree.heading("Nombre Producto", text="Nombre Producto")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Precio Venta", text="Precio Venta")
        self.tree.heading("Precio Compra", text="Precio Compra")

        # Establecer el ancho de las columnas
        self.tree.column("ID Producto", width=100, anchor="center")
        self.tree.column("Nombre Producto", width=200, anchor="center")
        self.tree.column("Cantidad", width=100, anchor="center")
        self.tree.column("Precio Venta", width=100, anchor="center")
        self.tree.column("Precio Compra", width=100, anchor="center")

        # Agregar algunos datos de ejemplo
        productos = [
            (1, "Producto A", 50, 100, 70),
            (2, "Producto B", 30, 120, 80),
            (3, "Producto C", 100, 150, 90)
        ]

        for producto in productos:
            self.tree.insert("", "end", values=producto)

        # Colocar el Treeview en la ventana
        self.tree.pack(padx=10, pady=10)

        # Ejecutar la aplicación
        self.ventana_productos.mainloop()
