class GestorDatos:
    def __init__(self):
        self.datos = {}
        self.siguiente_id = 1

    def crear(self, nombre, edad):
        id = self.siguiente_id
        self.datos[id] = {
            'Id': id,
            'Nombre': nombre,
            'Edad': edad
        }
        self.siguiente_id += 1
        return id

    def ver(self, id=None):
        if id is None:
            return self.datos
        return self.datos.get(id, "Registro no encontrado")

    def actualizar(self, id, nombre=None, edad=None):
        if id in self.datos:
            if nombre is not None:
                self.datos[id]['Nombre'] = nombre
            if edad is not None:
                self.datos[id]['Edad'] = edad
            return "Registro actualizado correctamente"
        return "Registro no encontrado"

    def eliminar(self, id):
        if id in self.datos:
            del self.datos[id]
            return "Registro eliminado correctamente"
        return "Registro no encontrado"

gestor = GestorDatos()


while True:
    print("\n   MENÚ   ")
    print("1. Crear usuario")
    print("2. Ver usuario")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")
    
    opcion = input("Elige una opción (1-5): ")
    
   
    if opcion == "1":
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        id = gestor.crear(nombre, edad)
        print(f"Usuario creado con ID: {id}")
    
    
    elif opcion == "2":
        print("Todos los usuarios:", gestor.ver())
    
    
    elif opcion == "3":
        id = int(input("ID del usuario a actualizar: "))
        nombre = input("Nuevo nombre: ")
        edad = int(input("Nueva edad: "))
        print(gestor.actualizar(id, nombre, edad))
    
    
    elif opcion == "4":
        id = int(input("ID del usuario a eliminar: "))
        print(gestor.eliminar(id))
    
    
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Intenta de nuevo.")
