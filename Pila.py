class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

class Pila:
    def __init__(self):
        self.tope = None

    def esta_vacia(self):
        return self.tope is None
    
    def agregar(self, valor):
        nodo_nuevo = Nodo(valor)
        nodo_nuevo.siguiente = self.tope
        self.tope = nodo_nuevo

    def eliminar(self):
        if self.esta_vacia():
            return None
        else:
            valor_eliminado = self.tope.valor
            self.tope = self.tope.siguiente
            return valor_eliminado
        
    def ver_tope(self):
        if self.esta_vacia():
            return None
        else:
            return self.tope.valor
        
    def recorrer(self):
        if self.esta_vacia():
            print("La pila está vacía")
        else:
            self._recorrer_aux(self.tope)

    def _recorrer_aux(self, nodo):
        if nodo is not None:
            print(nodo.valor.nombre)
            self._recorrer_aux(nodo.siguiente)
    
    def eliminar_uno_por_uno(self):
        while True:
            if  self.esta_vacia():
                break
            self.eliminar()

# Creamos algunas mascotas
mascota1 = Mascota("Luna", "Perro", 3)
mascota2 = Mascota("Simba", "Gato", 5)
mascota3 = Mascota("Bolt", "Perro", 2)
mascota3 = Mascota("Ares", "Perro", 2)

# Creamos una pila y agregamos las mascotas a la pila
pila_mascotas = Pila()
pila_mascotas.agregar(mascota1)
pila_mascotas.agregar(mascota2)
pila_mascotas.agregar(mascota3)

# Imprimimos todas las mascotas en la pila
pila_mascotas.recorrer()

pila_mascotas.eliminar()
print()
pila_mascotas.recorrer()