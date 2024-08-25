import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

class Inventario:
    def __init__(self, archivo_inventario='inventario.txt'):
        self.archivo_inventario = archivo_inventario
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo_inventario, 'r') as archivo:
                for linea in archivo:
                    id_producto, nombre, cantidad, precio = linea.strip().split(',')
                    self.productos[id_producto] = Producto(id_producto, nombre, int(cantidad), float(precio))
        except FileNotFoundError:
            print(f"El archivo {self.archivo_inventario} no existe. Se creará uno nuevo.")
            open(self.archivo_inventario, 'w').close()
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo_inventario, 'w') as archivo:
                for producto in self.productos.values():
                    archivo.write(str(producto) + '\n')
        except PermissionError:
            print(f"No se tiene permiso para escribir en {self.archivo_inventario}.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_inventario()
            print(f"Producto {producto.nombre} añadido exitosamente.")

    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nombre:
                producto.nombre = nombre
            if cantidad:
                producto.cantidad = cantidad
            if precio:
                producto.precio = precio
            self.guardar_inventario()
            print(f"Producto {id_producto} actualizado exitosamente.")
        else:
            print("El producto no existe en el inventario.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print(f"Producto {id_producto} eliminado exitosamente.")
        else:
            print("El producto no existe en el inventario.")
