import tkinter as tk
from tkinter import messagebox, ttk
from proyecto_final_nexus.model.Productos.producto import productos


class VentanaProductos:
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        # Crear la ventana secundaria
        self.ventana_productos = tk.Toplevel(self.parent)
        self.ventana_productos.title("Tabla de Productos")

        # Crear un marco para organizar los widgets
        frame_principal = tk.Frame(self.ventana_productos)
        frame_principal.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Usar grid en lugar de pack

        # Título
        self.titulo = ttk.Label(frame_principal, text="Listado De Productos", font=("Helvetica", 14))
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew", padx=10)  # Usar grid

        # Crear el Treeview
        self.tree = ttk.Treeview(frame_principal, columns=("ID Producto", "Nombre Producto", "Cantidad", "Precio Venta", "Precio Compra"), show="headings")

        # Configuración de las columnas
        self.tree.heading("ID Producto", text="ID Producto")
        self.tree.heading("Nombre Producto", text="Nombre Producto")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Precio Venta", text="Precio Venta")
        self.tree.heading("Precio Compra", text="Precio Compra")
        self.tree.column("ID Producto", width=100, anchor="center")
        self.tree.column("Nombre Producto", width=200, anchor="center")
        self.tree.column("Cantidad", width=100, anchor="center")
        self.tree.column("Precio Venta", width=100, anchor="center")
        self.tree.column("Precio Compra", width=100, anchor="center")

        # Colocar el Treeview en la ventana
        self.tree.grid(row=1, column=0, columnspan=2, pady=20, sticky="nsew")

        # Botón para regresar a la vista de afiliados
        btn_volver = tk.Button(frame_principal, text="Volver a Afiliados", command=self.ventana_productos.destroy)
        btn_volver.grid(row=2, column=0, columnspan=2, pady=10)  # Usar grid

        # Cargar los productos desde la base de datos
        self.cargar_productos()
    def cargar_productos(self):
        try:
            productos_analizar = productos.obtenerProductos()

            if productos_analizar:
                # Limpiar el Treeview antes de insertar nuevos datos
                for item in self.tree.get_children():
                    self.tree.delete(item)

                # Insertar los productos en el Treeview
                for producto in productos_analizar:
                    self.tree.insert("", "end", values=producto)
            else:
                messagebox.showinfo("Sin datos", "No se encontraron productos para mostrar.")

        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar los productos: {e}")



