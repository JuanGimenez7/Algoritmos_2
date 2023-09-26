class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

class Cola:
    def __init__(self):
        self.frente = None
        self.fin = None

    def esta_vacia(self):
        return self.frente is None

    def agregar(self, valor):
        nodo_nuevo = Nodo(valor)
        if self.esta_vacia():
            self.frente = nodo_nuevo
        else:
            self.fin.siguiente = nodo_nuevo
        self.fin = nodo_nuevo

    def eliminar(self):
        if self.esta_vacia():
            return None
        else:
            valor_eliminado = self.frente.valor
            self.frente = self.frente.siguiente
            if self.frente is None:
                self.fin = None
            return valor_eliminado
        
    def ver_frente(self):
        if self.esta_vacia():
            return None
        else:
            return self.frente.valor
        
    def recorrer(self):
        if self.esta_vacia():
            print("La cola está vacía")
        else:
            self._recorrer_aux(self.frente)
            
    def _recorrer_aux(self, nodo):
        if nodo is not None:
            print(nodo.valor.nombre)
            self._recorrer_aux(nodo.siguiente)

# Creamos algunas mascotas
mascota1 = Mascota("Luna", "Perro", 3)
mascota2 = Mascota("Simba", "Gato", 5)
mascota3 = Mascota("Bolt", "Perro", 2)

# Creamos una cola y agregamos las mascotas a la cola
cola_mascotas = Cola()
cola_mascotas.agregar(mascota1)
cola_mascotas.agregar(mascota2)
cola_mascotas.agregar(mascota3)

# Imprimimos todas las mascotas en la cola
cola_mascotas.recorrer()