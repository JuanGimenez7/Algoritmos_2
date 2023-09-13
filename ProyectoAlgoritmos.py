import csv
import json
import heapq

class Reservacion:
    def __init__(self, nombre_cliente, fecha_reserva, fecha_entrada, fecha_salida, numero_habitacion, duracion_estadia, tipo_habitacion, preferencias_alimentarias, numero_personas, contacto, precio_total, metodo_pago, notas_adicionales, estado_reservacion, hora_check_in_out, id_reservacion, correo_cliente):
        self.nombre_cliente = nombre_cliente
        self.fecha_reserva = fecha_reserva
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.numero_habitacion = numero_habitacion
        self.duracion_estadia = duracion_estadia
        self.tipo_habitacion = tipo_habitacion
        self.preferencias_alimentarias = preferencias_alimentarias
        self.numero_personas = numero_personas
        self.contacto = contacto
        self.precio_total = precio_total
        self.metodo_pago = metodo_pago
        self.notas_adicionales = notas_adicionales
        self.estado_reservacion = estado_reservacion
        self.hora_check_in_out = hora_check_in_out
        self.id_reservacion = id_reservacion
        self.correo_cliente = correo_cliente


class Funciones:

    def listar3(self, fecha1, fecha2):
        for reservacion in self.reservaciones:
            if fecha1 <= int(reservacion.fecha_reserva) <= fecha2:
                print(reservacion.nombre_cliente, reservacion.fecha_reserva, reservacion.precio_total)

    def listar4(self):
        for reservacion in self.reservaciones:
            print(reservacion.nombre_cliente, reservacion.numero_personas)
    
    def listar5(self):
        for reservacion in self.reservaciones:
            print(reservacion.nombre_cliente, reservacion.duracion_estadia)
            
    def __init__(self):
        self.reservaciones = []
        
    def cargar_reservaciones_desde_csv(self, archivo):
        self.reservaciones = []
        with open(archivo, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                reservacion = Reservacion(
                    row["Nombre del Cliente"],
                    row["Fecha de Reserva"],
                    row["Fecha de Entrada"],
                    row['Fecha de Salida'],
                    row['Número de Habitación'],
                    int(row['Duración de la Estadía']),
                    row['Tipo de Habitación'],
                    row['Preferencias Alimentarias'],
                    int(row['Número de Personas']),
                    row['Contacto'],
                    float(row['Precio Total']),
                    row['Método de Pago'],
                    row['Notas Adicionales'],
                    row['Estado de la Reservación'],
                    row['Hora de Check-in/Check-out'],
                    row['ID de Reservación'],
                    row['Correo del Cliente']
                )
                self.reservaciones.append(reservacion)
        return self.reservaciones

    def cargar_reservaciones_desde_json(self, archivo):
        self.reservaciones = []
        with open(archivo, 'r') as file:
            data = json.load(file)
            for item in data:
                reservacion = Reservacion(
                    item['nombre_cliente'],
                    item['fecha_reserva'],
                    item['fecha_entrada'],
                    item['fecha_salida'],
                    item['num_habitacion'],
                    item['duracion_estadia'],
                    item['tipo_habitacion'],
                    item['preferencias_alimentarias'],
                    item['num_personas'],
                    item['contacto'],
                    item['precio_total'],
                    item['metodo_pago'],
                    item['notas_adicionales'],
                    item['estado_reservacion'],
                    item['hora_checkin_checkout'],
                    item['id_reservacion'],
                    item['correo_cliente']
                )
                self.reservaciones.append(reservacion)
        return self.reservaciones


#METODO HEAPSORT PARA ORDENAR DE MANERA ASCENDENTE LAS RESERVACIONES SEGUN SU DURACION DE ESTADIA
    def heapifyascendente(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i].duracion_estadia < arr[l].duracion_estadia:
            largest = l

        if r < n and arr[largest].duracion_estadia < arr[r].duracion_estadia:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]

            self.heapifyascendente(arr, n, largest)


    def heapsortascendente(self, arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapifyascendente(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapifyascendente(arr, i, 0)

#METODO HEAPSORT PARA ORDENAR DE MANERA DESCENDENTE LAS RESERVACIONES SEGUN SU DURACION DE ESTADIA
    def heapifydescendente(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i].duracion_estadia > arr[l].duracion_estadia:
            largest = l

        if r < n and arr[largest].duracion_estadia > arr[r].duracion_estadia:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]

            self.heapifydescendente(arr, n, largest)

    def heapsortdescendente(self, arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapifydescendente(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapifydescendente(arr, i, 0)

#METODO SHELLSORT PARA ORDENAR DE MANERA ASCENDENTE EL NUMERO DE PERSONAS
    def shellsortascendente(self, lista):
        n = len(lista)
        brecha = n // 2
        while brecha > 0:
            for i in range(brecha, n):
                temp = lista[i].numero_personas
                j = i
                while j >= brecha and lista[j - brecha].numero_personas > temp:
                    lista[j].numero_personas = lista[j - brecha].numero_personas
                    j -= brecha
                lista[j].numero_personas = temp
            brecha //= 2
        return lista
    
#METODO SHELLSORT PARA ORDENAR DE MANERA DESCENDENTE EL NUMERO DE PERSONAS
    def shellsortdescendente(self, lista):
        n = len(lista)
        brecha = n // 2
        while brecha > 0:
            for i in range(brecha, n):
                temp = lista[i].numero_personas
                j = i
                while j >= brecha and lista[j - brecha].numero_personas < temp:
                    lista[j].numero_personas = lista[j - brecha].numero_personas
                    j -= brecha
                lista[j].numero_personas = temp
            brecha //= 2
        return lista

#METODO MERGESORT PARA ORDENAR PRECIO ASCENDENTE
    def merge_sort(self, list):
        list_length = len(list)
        if list_length == 1:
            return list
        mid_point = list_length // 2
        left_partition = self.merge_sort(list[:mid_point])
        right_partition = self.merge_sort(list[mid_point:])
        return self.merge(left_partition, right_partition)

    def merge(self, left, right):
        output = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].fecha_reserva < right[j].fecha_reserva:
                output.append(left[i].fecha_reserva)
                i += 1
            else:
                output.append(right[j].fecha_reserva)
                j += 1
        output.extend(left[i:].fecha_reserva)
        output.extend(right[j:].fecha_reserva)
        return output

#MENU
            
manager = Funciones()
manager.cargar_reservaciones_desde_json("datos.json")

print("Menu de Ordenamiento de Reservaciones")
print("-----------------Opciones-----------------")
print("-Opcion 1:")
print("-Opcion 3: Ordenar el precio con un rango de fechas de reserva dada")
print("-Opcion 4: Ordenar reservaciones según numero de personas")
print("-Opcion 5: Ordenar reservaciones según su duración de estadía")
opc = int(input("Ingrese la opcion de ordenamiento a elegir: "))
#if opc == 1:

#elif opc == 2:

#elif opc == 3:

#elif opc == 4:
    
if opc == 5:
    print("Escoja la forma en que serán ordenadas las reservaciones")
    print("1. Ascendente")
    print("2. Descendente")
    opc5 = int(input("Ingrese la opción a elegir: "))
    if opc5 == 1:
        manager.heapsortascendente(manager.reservaciones)
        print("Las reservaciones ordenadas de forma ascendente en base a su duracion de estadia son las siguientes:")
        manager.listar5()
    elif opc5 == 2:
        manager.heapsortdescendente(manager.reservaciones)
        print("Las reservaciones ordenadas de forma ascendente en base a su duracion de estadia son las siguientes:")
        manager.listar5()        

elif opc == 4:
    print("Escoja la forma en que serán ordenadas el numero de personas")
    print("1. Ascendente")
    print("2. Descendente")  
    opc4 = int(input("Ingrese la opción a elegir: ")) 
    if opc4 == 1:
        manager.shellsortascendente(manager.reservaciones)
        print("Las reservaciones ordenadas de forma ascendente en base a su numero de personas:")
        manager.listar4()    
    elif opc4 == 2:
        manager.shellsortdescendente(manager.reservaciones)
        print("Las reservaciones ordenadas de forma descendente en base a su numero de personas:")
        manager.listar4()

elif opc == 3:
    print("Escoja la forma en que serán ordenados los precios totales")
    print("1. Ascendente")
    print("2. Descendente")
    opc3 = int(input("Ingrese la opción a elegir: "))
    print("Escoja el rango de las fechas de reserva")
    a1 = input("año de inicio: ")
    m1 = input("mes de inicio: ")
    d1 = input("dia de inicio: ")
    t1 = int(a1 + m1 + d1)
    a2 = input("año de fin: ")
    m2 = input("mes de fin: ")
    d2 = input("dia de fin: ")
    t2 = int(a2 + m2 + d2)
    if opc == 1:
        manager.shellsortascendente(manager.reservaciones)
        print("Las reservaciones ordenadas por el precio de forma ascendente en el rango de fecha dado es:")
        manager.listar3(t1, t2) 
        
    
else:
    print("La opcion elegida no es correcta")



