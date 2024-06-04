

class Producto:
    def __init__(self, codigo_de_barras, nombre, precio):
        self.__codigo_de_barras__ = codigo_de_barras
        self.__nombre__ = nombre
        self.__precio__ = precio


class ProductosComprados:
    def __init__(self, producto, cantidad):
        self.__producto__ = producto
        self.__cantidad__ = cantidad

    def calcular_total(self):
        return self.__cantidad__ * self.__producto__.__precio__


class Compra:
    def __init__(self):
        self.__productos_comprados__ = []

    def agregar_producto(self, producto_comprado):
        self.__productos_comprados__.append(producto_comprado)  

    @property
    def total(self):
        precio_total = 0

        for producto_comprado in self.__productos_comprados__:
            precio_producto_comprado = producto_comprado.calcular_total()
            precio_total += precio_producto_comprado
        return precio_total


# Productos en gondola
fideo = Producto(1, "Fideos Matarazzo", 1200)
yerba = Producto(2, "Yerba Taragui", 2000)

# Creamos los productos comprados
compra = Compra()

fideo_comprados = ProductosComprados(fideo, 3)
yerba_compradas = ProductosComprados(yerba, 2)

# Agregamos los productos comprados a la compra
compra.agregar_producto(fideo_comprados)
compra.agregar_producto(yerba_compradas)

print(compra.total)





















