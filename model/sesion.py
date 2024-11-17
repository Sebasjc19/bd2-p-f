# Clase que representa al Afiliado
class Sesion:
    def __init__(self, id_afiliado, id_rango, id_promotor, nombre, apellido,
                 email, fecha_afiliacion, telefono, activo):
        self.id_afiliado = id_afiliado  # ID único del afiliado
        self.id_rango = id_rango  # ID del rango del afiliado (puede referir a un nivel o categoría)
        self.id_promotor = id_promotor  # ID del promotor relacionado con el afiliado
        self.nombre = nombre  # Nombre del afiliado
        self.apellido = apellido  # Apellido del afiliado
        self.email = email  # Correo electrónico del afiliado
        self.fecha_afiliacion = fecha_afiliacion  # Fecha de afiliación
        self.telefono = telefono  # Número de teléfono del afiliado
        self.activo = activo  # Estado de la cuenta del afiliado (activo/inactivo)
