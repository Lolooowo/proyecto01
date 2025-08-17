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
        #nombre = str
        #precio = float
        #stock = int
        #codigo = int
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
                    precio = float(input("Ingrese el precio del producto: Q."))
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
        self.productos[codigo] = {
            "producto": nuevo_producto
        }
        print("Producto ingresado correctamente")
        input()
    def eliminar_producto(self, codigo):
        if codigo in self.productos.keys():
            del self.productos[codigo]
            print("Producto eliminado correctamente")
        else:
            print("No existe el producto ingresado")

class Ordenador:
    def __init__(self):
        self.ordenadosNombre = []
        self.ordenadosPrecio = []
        self.ordenadosStock = []
    def ordenamientoNombre(self, productos):
        lista = list(productos.items())
        if len(lista) <= 1:
            return lista
        else:
            pivote = lista[0]
            mayores = [x for x in lista[1:] if x[1]["producto"].nombre > pivote[1]["producto"].nombre]
            iguales = [x for x in lista if x[1]["producto"].nombre == pivote[1]["producto"].nombre]
            menores = [x for x in lista[1:] if x[1]["producto"].nombre < pivote[1]["producto"].nombre]
            return self.ordenamientoNombre(dict(menores)) + iguales + self.ordenamientoNombre(dict(mayores))
    def ordenamientoPrecio(self, productos):
        lista = list(productos.items())
        if len(lista) <= 1:
            return lista
        else:
            pivote = lista[0]
            mayores = [x for x in lista[1:] if x[1]["producto"].precio > pivote[1]["producto"].precio]
            iguales = [x for x in lista if x[1]["producto"].precio == pivote[1]["producto"].precio]
            menores = [x for x in lista[1:] if x[1]["producto"].precio < pivote[1]["producto"].precio]
            return self.ordenamientoNombre(dict(menores)) + iguales + self.ordenamientoNombre(dict(mayores))
    def ordenamientoStock(self, productos):
        lista = list(productos.items())
        if len(lista) <= 1:
            return lista
        else:
            pivote = lista[0]
            mayores = [x for x in lista[1:] if x[1]["producto"].stock > pivote[1]["producto"].stock]
            iguales = [x for x in lista if x[1]["producto"].stock == pivote[1]["producto"].stock]
            menores = [x for x in lista[1:] if x[1]["producto"].stock < pivote[1]["producto"].stock]
            return self.ordenamientoNombre(dict(menores)) + iguales + self.ordenamientoNombre(dict(mayores))
class Buscador:
    def __init__(self):
        self.busquedas = {}
    def buscar(self, codigo):
        for clave, valor in GestionProducto.productos.items():
            if clave == codigo:
                self.busquedas[clave] = {
                    "producto": valor
                }
                print("Producto Encontrado.")
                input()
                print(f"\tcodigo: {clave}")
                print(valor["producto"])
            else:
                print("No existe el producto ingresado")




GestionProducto = GestionProducto()
Ordenador = Ordenador()
Buscador = Buscador()

while True:
    print("1. Ingreso Producto")
    print("2. Mostrar Productos")
    print("3. Buscar Productos")
    print("4. Gestionar Productos")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))
    match opcion:
        case 1:
            GestionProducto.ingreso_productos()
        case 2:
            print("Mostrar Productos")
            print("1. Mostrar Productos por Precio")
            print("2. Mostrar Productos por Stock")
            print("3. Mostrar Productos por Nombre")
            print("4. Salir al menú principal")
            opcion2 = int(input("Ingrese una opcion: "))
            match opcion2:
                case 1:
                    Ordenador.ordenadosPrecio = Ordenador.ordenamientoPrecio(GestionProducto.productos)
                    preciosDict = dict(Ordenador.ordenadosPrecio)
                    for clave, valor in preciosDict.items():
                        print(f"\tCódigo del producto: {clave}")
                        print(valor["producto"])
                case 2:
                    Ordenador.ordenadosStock = Ordenador.ordenamientoStock(GestionProducto.productos)
                    stockDict = dict(Ordenador.ordenadosStock)
                    for clave, valor in stockDict.items():
                        print(f"\tCódigo del producto: {clave}")
                        print(valor["producto"])
                case 3:
                    Ordenador.ordenadosNombre = Ordenador.ordenamientoNombre(GestionProducto.productos)
                    nombreDict = dict(Ordenador.ordenadosNombre)
                    for clave, valor in nombreDict.items():
                        print(f"\tCódigo del producto: {clave}")
                        print(valor["producto"])
                case 4:
                    print("Saliendo al menú principal....")
                    break
                case _:
                    print("Ingrese una opcion correcta")
        case 3:
            buscado = input("Ingrese el codigo del producto: ")
            Buscador.buscar(buscado)
        case 4:
            pass
        case 5:
            print("Saliendo del programa....")
            break
        case _:
            print("Ingrese una opcion correcta")










