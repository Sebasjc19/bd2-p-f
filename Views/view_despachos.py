import tkinter as tk
from tkinter import ttk

class VentanaDespachos:
    def __init__(self, parent):
            self.parent = parent

            # Crear la ventana secundaria
            self.ventana_despachos = tk.Toplevel(self.parent)
            self.ventana_despachos.title("Administración de Despachos")
            self.ventana_despachos.geometry("900x500")

            # Establecer un estilo con ttk
            estilo = ttk.Style()
            estilo.configure("TButton", font=("Helvetica", 8), padding=3)
            estilo.configure("TLabel", font=("Helvetica", 10), padding=5)
            estilo.configure("TEntry", font=("Helvetica", 10), padding=5)

            # Crear un marco para contener los botones y el Treeview
            self.frame_principal = tk.Frame(self.ventana_despachos)
            self.frame_principal.pack(padx=20, pady=20, fill="both", expand=True)

            # Título de la ventana centrado
            self.titulo = ttk.Label(self.frame_principal, text="Administración de Despachos", font=("Helvetica", 14))
            self.titulo.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew", padx=10)

            self.boton_volver = ttk.Button(self.frame_principal, text="Volver", command= self.ventana_despachos.destroy)
            self.boton_volver.grid(row=1, column=0, padx=5, pady=10, sticky="ew", ipadx=10)

            self.boton_reporte = ttk.Button(self.frame_principal, text="Generar Reporte")
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
            self.tree = ttk.Treeview(self.frame_tabla, columns=("ID Despacho", "ID Factura Venta", "ID Dirección",
                                                                "ID Transportadora", "Fecha Salida", "Hora Salida", "Guía"),
                                     show="headings")

            # Definir las columnas
            self.tree.heading("ID Despacho", text="ID Despacho")
            self.tree.heading("ID Factura Venta", text="ID Factura Venta")
            self.tree.heading("ID Dirección", text="ID Dirección")
            self.tree.heading("ID Transportadora", text="ID Transportadora")
            self.tree.heading("Fecha Salida", text="Fecha Salida")
            self.tree.heading("Hora Salida", text="Hora Salida")
            self.tree.heading("Guía", text="Guía")

            # Ajustar el ancho de las columnas
            for col in ("ID Despacho", "ID Factura Venta", "ID Dirección", "ID Transportadora",
                        "Fecha Salida", "Hora Salida", "Guía"):
                self.tree.column(col, width=120, anchor="center")

            # Agregar algunos datos de ejemplo
            self.despachos = [
                (1, 2, 3, 4, "1/3/2020", "10:00 pm", 100),
                (32, 33, 34, 38, "2/2/2021", "2:00 am", 2356),
                (35, 36, 37, 39, "3/4/2022", "5:00 pm", 3123)
            ]


            # Crear una barra de desplazamiento
            self.scrollbar = tk.Scrollbar(self.frame_tabla, orient="vertical")
            self.tree.configure(yscrollcommand=self.scrollbar.set)
            self.scrollbar.grid(row=1, column=2, sticky="ns")

            # Colocar el Treeview en la ventana
            self.tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

            # Configurar las filas y columnas para que se expandan
            self.frame_tabla.grid_rowconfigure(1, weight=1)
            self.frame_tabla.grid_columnconfigure(0, weight=1)

        # Ejecutar la aplicación
            self.ventana_despachos.mainloop()
