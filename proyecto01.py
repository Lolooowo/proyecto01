class Producto:
    def __init__(self,nombre,precio, stock, categoria):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.precio} | Categoria: {self.categoria} | Stock: {self.stock}"
class GestionProducto:
    def __init__(self):
        self.productos = {}
    def ingreso_productos(self):
        while True:
            try:
                codigo = int(input("Ingrese el codigo del producto: "))
                if codigo in self.productos.keys():
                    print(f"(CodigoDuplicadoError)")
                    print()
                else:
                    return False
            except(ValueError):
                print("El codigo no es valido")
                input()
        while True:
            nombre = input("Ingrese el nombre del producto: ")

GestionProducto = GestionProducto()

while True:
    print("1. Ingreso Producto")
    print("2. Mostrar Productos")
    print("3. Buscar Productos")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))
    match opcion:
        case 1:
            GestionProducto.ingreso_productos()








