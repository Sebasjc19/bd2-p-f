import tkinter as tk
from tkinter import messagebox, ttk

# Clase para la ventana de productos
class VentanaVentas:
    def __init__(self, parent):
        self.parent = parent
        # Crear la ventana secundaria
        self.ventana_ventas = tk.Toplevel(self.parent)  # Ventana secundaria
        self.ventana_ventas.title("Tabla de ventas")

        # Crear un Treeview para mostrar la tabla
        self.tree = ttk.Treeview(self.ventana_ventas, columns=("ID Factura", "Fecha", "Total"), show="headings")

        # Definir las columnas
        self.tree.heading("ID Factura", text="ID Factura")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Total", text="Total")

        # Establecer el ancho de las columnas
        self.tree.column("ID Factura", width=100, anchor="center")
        self.tree.column("Nombre afiliados", width=200, anchor="center")
        self.tree.column("Total", width=100, anchor="center")

        # Agregar algunos datos de ejemplo
        ventas = [
            (1, "1/1/2020", 100),
            (32, "2/2/2021", 2356),
            (35, "3/3/2022", 3123)
        ]

        for venta in ventas:
            self.tree.insert("", "end", values=venta)

        # Colocar el Treeview en la ventana
        self.tree.pack(padx=10, pady=10)

        # Ejecutar la aplicación
        self.ventana_ventas.mainloop()
