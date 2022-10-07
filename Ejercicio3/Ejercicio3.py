class Producto:
    def __innit__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print("El producto s eha creado con éxito")
    
    def __str__(self):
        return "Código:", self.codigo, "Nombre:", self.nombre, "Precio:", self.precio, "Tipo", self.tipo

producto1=Producto(2381, "Ngolo", 10, "Negro")
print(producto1)
producto1=Producto(2381, "Ngolo", 10, "Negro")
