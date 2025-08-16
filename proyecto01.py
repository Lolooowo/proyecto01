class Producto:
    def __init__(self,nombre,precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.precio} | Stock: {self.stock}"
class GestionProducto:
    def __init__(self):
        self.productos = {}
    def ingreso_productos(self):
        nombre = str
        precio = float
        stock = int
        codigo = int
        while True:
            try:
                codigo = int(input("Ingrese el codigo del producto: "))
                if codigo in self.productos.keys():
                    print(f"(CodigoDuplicadoError)")
                    print()
                else:
                    break
            except(ValueError):
                print("cantidad ingresada incorrecta")
                input()
        while True:
            try:
                nombre = input("Ingrese el nombre del producto: ")
                while True:
                    precio = float(input("Ingrese el precio del producto: "))
                    if precio < 0:
                        print("No se pueden ingresar un precio negativo")
                    else:
                        break
                while True:
                    stock = int(input("Ingrese el stock del producto: "))
                    if stock < 0:
                        print("No se pueden ingresa una cantidad de productos negativas")
                    else:
                        break
                break
            except(ValueError):
                print("Ingrese el valor que se especifica")
                input()
            nuevo_producto = Producto(nombre, precio, stock)



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








