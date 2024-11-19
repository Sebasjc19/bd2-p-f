import tkinter as tk
from tkinter import messagebox, ttk


import tkinter as tk
from tkinter import ttk

class VentanaVentas:
    def __init__(self, parent):
        self.parent = parent

        # Crear la ventana secundaria
        self.ventana_ventas = tk.Toplevel(self.parent)
        self.ventana_ventas.title("Administración de Ventas")
        self.ventana_ventas.geometry("900x500")  # Ajusté el tamaño para más espacio

        # Establecer un estilo con ttk
        estilo = ttk.Style()
        estilo.configure("TButton", font=("Helvetica", 8), padding=3)  # Botones más pequeños
        estilo.configure("TLabel", font=("Helvetica", 10), padding=5)
        estilo.configure("TEntry", font=("Helvetica", 10), padding=5)

        # Crear un marco principal
        self.frame_principal = tk.Frame(self.ventana_ventas)
        self.frame_principal.pack(padx=20, pady=20, fill="both", expand=True)

        # Título de la ventana
        self.titulo = ttk.Label(self.frame_principal, text="Administración de Ventas", font=("Helvetica", 14))
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew", padx=10)

        # Botones de la ventana
        self.boton_volver = ttk.Button(self.frame_principal, text="Volver", command= self.ventana_ventas.destroy)
        self.boton_volver.grid(row=1, column=0, padx=5, pady=10, sticky="ew", ipadx=10)

        self.boton_reporte = ttk.Button(self.frame_principal, text="Reporte Productos")
        self.boton_reporte.grid(row=1, column=1, padx=5, pady=10, sticky="ew", ipadx=10)

        # Crear un marco para contener el Treeview y la barra de búsqueda
        self.frame_tabla = tk.Frame(self.frame_principal)
        self.frame_tabla.grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")

        # Crear una barra de búsqueda
        self.label_buscar = ttk.Label(self.frame_tabla, text="Buscar:")
        self.label_buscar.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_buscar = ttk.Entry(self.frame_tabla, width=30)
        self.entry_buscar.grid(row=0, column=1, padx=5, pady=5)
        self.entry_buscar.bind("<KeyRelease>")

        # Crear un Treeview para mostrar la tabla
        self.tree = ttk.Treeview(self.frame_tabla, columns=("ID Factura", "Fecha", "Nombre Afiliados", "Total"),
                                 show="headings")


        self.tree.heading("ID Factura", text="ID Factura")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Nombre Afiliados", text="Nombre Afiliados")
        self.tree.heading("Total", text="Total")

        # Ajustar el ancho de las columnas
        for col in ("ID Factura", "Fecha", "Nombre Afiliados", "Total"):
            self.tree.column(col, width=120, anchor="center")

        # Agregar algunos datos de ejemplo
        ventas = [
            (1, "1/1/2020", "Miguel", 100),
            (32, "2/2/2021", "Ángel", 2356),
            (35, "3/3/2022", "Garcia", 3123)
        ]
        for venta in ventas:
            self.tree.insert("", "end", values=venta)

        # Crear una barra de desplazamiento vertical
        self.scrollbar = tk.Scrollbar(self.frame_tabla, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=2, sticky="ns")

        # Colocar el Treeview en la ventana
        self.tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Configurar las filas y columnas para que se expandan
        self.frame_tabla.grid_rowconfigure(1, weight=1)
        self.frame_tabla.grid_columnconfigure(0, weight=1)

        # Ejecutar la aplicación
        self.ventana_ventas.mainloop()


