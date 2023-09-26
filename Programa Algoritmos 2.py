# Importar bibliotecas necesarias
import datetime
import json
import csv
# Lista de hoteles
hoteles = []

# Definir clases

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.reservaciones = LinkedList()
        self.disponible = True

# Definición de la clase Reservacion
class Reservacion:
    def __init__(self, nombre_huesped, fecha_entrada, fecha_salida):
        self.nombre_huesped = nombre_huesped
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida

#Definicion de la clase Hotel
class Hotel:
    def __init__(self, nombre, direccion, numero_telefono, habitaciones_disponibles, reserva):
        self.nombre = nombre
        self.direccion = direccion
        self.numero_telefono = numero_telefono
        self.habitaciones_disponibles = habitaciones_disponibles
        self.reserva = reserva

    def crear_hotel():
        # Solicitar los datos del hotel
        nombre = input("Ingrese el nombre del hotel: ")
        direccion = input("Ingrese la dirección del hotel: ")
        numero_telefono = input("Ingrese el número de teléfono del hotel: ")
        habitaciones_disponibles = list(input("Ingrese el número de las habitaciones disponibles: "))
        reserva = list(input("Ingrese el número de las habitaciones reservadas del hotel: "))
        # Crear el hotel
        hotel = Hotel(nombre, direccion, numero_telefono, habitaciones_disponibles, reserva)

        # Agregar el hotel a la lista
        hoteles.append(hotel)

        print("Hotel creado")

    def buscar_hotel(nombre_hotel):
        # Buscar el hotel en la lista
        for hotel in hoteles:
            if hotel.nombre == nombre_hotel:
                return hotel

        # El hotel no existe
        return None

    def modificar_hotel():
        # Solicitar el nombre del hotel a modificar
        nombre_hotel = input("Ingrese el nombre del hotel a modificar: ")

        # Buscar el hotel
        hotel = Hotel.buscar_hotel(nombre_hotel)

        # Solicitar los datos a modificar
        if hotel:
            nombre = input("Ingrese el nuevo nombre del hotel: ")
            direccion = input("Ingrese la nueva dirección del hotel: ")
            numero_telefono = input("Ingrese el nuevo número de teléfono del hotel: ")
            habitaciones_disponibles = list(input("Ingrese el número de las habitaciones disponibles: "))
            reserva = list(input("Ingrese el número de las habitaciones reservadas del hotel: "))
            # Modificar los datos del hotel
            Hotel.nombre = nombre
            Hotel.direccion = direccion
            Hotel.numero_telefono = numero_telefono
            Hotel.habitaciones_disponibles = habitaciones_disponibles
            Hotel.reserva = reserva

            print("Hotel modificado")
        else:
            print("El hotel no existe")

    def eliminar_hotel():
        # Solicitar el nombre del hotel a eliminar
        nombre_hotel = input("Ingrese el nombre del hotel a eliminar: ")

        # Buscar el hotel
        hotel = Hotel.buscar_hotel(nombre_hotel)

        # Eliminar el hotel
        if hotel:
            hoteles.remove(hotel)
            print("Hotel eliminado")
        else:
            print("El hotel no existe")

    def listar_hoteles():
        print("-----------Lista de Hoteles-------------")
        for hotel in hoteles:
            print("--------------Hotel----------------")
            print(f"Nombre: {hotel.nombre}")
            print(f"Dirección: {hotel.direccion}")
            print(f"Teléfono: {hotel.numero_telefono}")
            print(f"Habitaciones disponibles: {hotel.habitaciones_disponibles}")
            print(f"Habitaciones reservadas: {hotel.reserva}")
            print("---------------------------------")


    def guardar_datos(nombre_archivo, tipo_archivo):
        # Abrir el archivo en modo escritura
        with open(nombre_archivo, "w") as archivo:
            # Escribir los datos del sistema en el archivo
            if tipo_archivo == "csv":
                # Guardar los datos en formato CSV
                archivo.write("nombre,direccion,telefono\n")
                for hotel in hoteles:
                    archivo.write(f"{hotel.nombre},{hotel.direccion},{hotel.numero_telefono}\n")
            elif tipo_archivo == "json":
                # Guardar los datos en formato JSON
                archivo.write(json.dumps(hoteles))

    def cargar_datos(nombre_archivo):
        # Abrir el archivo en modo lectura
        with open(nombre_archivo, "r") as archivo:
            # Leer los datos del archivo
            if archivo.readline().strip() == "nombre,direccion,telefono":
                # Leer los datos en formato CSV
                for linea in archivo:
                    # Separar los datos de la línea
                    datos = linea.strip().split(",")

                    # Crear un nuevo hotel
                    hotel = Hotel(datos[0], datos[1], datos[2])

                    # Agregar el hotel a la lista de hoteles
                    hoteles.append(hotel)
            elif archivo.readline().strip() == "{" and archivo.readline().strip() == "}":
                # Leer los datos en formato JSON
                datos = json.loads(archivo.read())

                # Agregar los hoteles a la lista de hoteles
                hoteles = datos


    def crear_habitacion(self, numero_habitacion, tipo_habitacion, tarifa):
        habitacion = Habitacion(numero_habitacion, tipo_habitacion, tarifa)
        self.habitaciones_disponibles[numero_habitacion] = habitacion

    def modificar_habitacion(self, numero_habitacion, tipo_habitacion, tarifa):
        habitacion = self.habitaciones_disponibles[numero_habitacion]
        habitacion.tipo_habitacion = tipo_habitacion
        habitacion.tarifa = tarifa

    def eliminar_habitacion(self, numero_habitacion):
        del self.habitaciones_disponibles[numero_habitacion]

    def crear_reserva(self, fecha_inicio, fecha_fin, numero_personas, numero_habitaciones, datos_cliente):
        reserva = Reservacion(fecha_inicio, fecha_fin, numero_personas, numero_habitaciones, datos_cliente)
        self.reservas.append(reserva)

    def modificar_reserva(self, numero_reserva, fecha_inicio, fecha_fin, numero_personas, numero_habitaciones, datos_cliente):
        reserva = self.reservas[numero_reserva]
        reserva.fecha_inicio = fecha_inicio
        reserva.fecha_fin = fecha_fin
        reserva.numero_personas = numero_personas
        reserva.numero_habitaciones = numero_habitaciones
        reserva.datos_cliente = datos_cliente

    def eliminar_reserva(self, numero_reserva):
        del self.reservas[numero_reserva]

    def consultar_habitacion(self, numero_habitacion):
        return self.habitaciones_disponibles[numero_habitacion]

    def consultar_reserva(self, numero_reserva):
        return self.reservas[numero_reserva]

    def listar_habitaciones(self):
        return list(self.habitaciones_disponibles.values())

    def listar_reservas(self):
        return self.reservas

    def ordenar_habitaciones(self, criterio):
        if criterio == "nombre":
            self.habitaciones_disponibles = sorted(self.habitaciones_disponibles.values(), key=lambda x: x.nombre)
        elif criterio == "tipo_habitacion":
            self.habitaciones_disponibles = sorted(self.habitaciones_disponibles.values(), key=lambda x: x.tipo_habitacion)
        elif criterio == "tarifa":
            self.habitaciones_disponibles = sorted(self.habitaciones_disponibles.values(), key=lambda x: x.tarifa)
        else:
            raise ValueError("Criterio de ordenamiento no válido")

    def ordenar_reservas(self, criterio):
        if criterio == "fecha_inicio":
            self.reservas = sorted(self.reservas, key=lambda x: x.fecha_inicio)
        elif criterio == "fecha_fin":
            self.reservas = sorted(self.reservas, key=lambda x: x.fecha_fin)
        elif criterio == "numero_personas":
            self.reservas = sorted(self.reservas, key=lambda x: x.numero_personas)
        elif criterio == "numero_habitaciones":
            self.reservas = sorted(self.reservas, key=lambda x: x.numero_habitaciones)
        else:
            raise ValueError("Criterio de ordenamiento no válido")

    def generar_informe_hoteles(self):
        informe = ""
        informe += f"**Listado de hoteles:**\n"
        for hotel in self.habitaciones_disponibles:
            informe += f"* {Hotel.nombre}\n"
            informe += f"    Dirección: {Hotel.direccion}\n"
            informe += f"    Número de teléfono: {Hotel.numero_telefono}\n"
            informe += f"    **Habitaciones disponibles:**\n"
            for habitacion in self.habitaciones_disponibles.values():
                informe += f"        * Número: {habitacion.numero_habitacion}\n"
                informe += f"            * Tipo: {habitacion.tipo_habitacion}\n"
                informe += f"            * Tarifa: {habitacion.tarifa}\n"
        return informe
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

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

def menu():
    print("**Menú de opciones**")
    print("1. Crear hotel")
    print("2. Modificar hotel")
    print("3. Eliminar hotel")
    print("4. Crear habitación")
    print("5. Modificar habitación")
    print("6. Eliminar habitación")
    print("7. Cargar Datos")
    print("8. Guardar Datos")
    print("9. Generar informes")
    print("10. Salir")

    # Obtener la opción del usuario
    opcion = input("Ingrese una opción: ")

    # Ejecutar la opción seleccionada
    if opcion == "1":
        Hotel.crear_hotel()
    elif opcion == "2":
        Hotel.modificar_hotel()
    elif opcion == "3":
        Hotel.eliminar_hotel()
    elif opcion == "4":
        Hotel.crear_habitacion()
    elif opcion == "5":
        Hotel.modificar_habitacion()
    elif opcion == "6":
        Hotel.eliminar_habitacion()
    elif opcion == "7":
        Hotel.cargar_datos("hoteles.json")
    elif opcion == "8":
        Hotel.guardar_datos("hoteles.json", "json")
    elif opcion == "9":
        Hotel.listar_hoteles()
    elif opcion == "10":
        print("Saliendo del sistema...")
        exit()
    else:
        print("Opción no válida")

# Bucle principal

while True:
    menu()
