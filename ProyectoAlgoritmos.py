import csv
import json
from datetime import datetime

#CREACION DE CLASE RESERVACION
class Reservacion:
#CONSTRUCTOR
    def __init__(self, nombre_cliente, fecha_reserva, fecha_entrada, fecha_salida, num_habitacion, duracion_estadia, tipo_habitacion, preferencias_alimentarias, num_personas, contacto, precio_total, metodo_pago, notas_adicionales, estado_reservacion, hora_checkin_checkout, id_reservacion, correo_cliente):
        self.nombre_cliente = nombre_cliente
        self.fecha_reserva = fecha_reserva
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.num_habitacion = num_habitacion
        self.duracion_estadia = duracion_estadia
        self.tipo_habitacion = tipo_habitacion
        self.preferencias_alimentarias = preferencias_alimentarias
        self.num_personas = num_personas
        self.contacto = contacto
        self.precio_total = precio_total
        self.metodo_pago = metodo_pago
        self.notas_adicionales = notas_adicionales
        self.estado_reservacion = estado_reservacion
        self.hora_checkin_checkout = hora_checkin_checkout
        self.id_reservacion = id_reservacion
        self.correo_cliente = correo_cliente

#CREACION DE CLASE SISTEMA RESERVACIONES
class SistemaReservaciones:
#CONSTRUCTOR
    def __init__(self):
        self.reservaciones = []

#FUNCION CARGAR RESERVACIONES PARA ARCHIVOS .csv o .json
    def cargar_datos(self, archivo):
        if archivo.endswith('.csv'):
            with open(archivo, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    reservacion = Reservacion(
                        row['Nombre Cliente'],
                        datetime.strptime(row['Fecha Reserva'], '%Y-%m-%d'),
                        datetime.strptime(row['Fecha Entrada'], '%Y-%m-%d'),
                        datetime.strptime(row['Fecha Salida'], '%Y-%m-%d'),
                        int(row['Número de Habitación']),
                        int(row['Duración de Estadía']),
                        row['Tipo de Habitación'],
                        row['Preferencias Alimentarias'],
                        int(row['Número de Personas']),
                        row['Contacto'],
                        float(row['Precio Total']),
                        row['Método de Pago'],
                        row['Notas Adicionales'],
                        row['Estado de la Reservación'],
                        row['Hora de Check-in/Check-out'],
                        int(row['ID de Reservación']),
                        row['Correo del Cliente']
                    )
                    self.reservaciones.append(reservacion)
        elif archivo.endswith('.json'):
            with open(archivo, 'r') as file:
                data = json.load(file)
                for item in data:
                    reservacion = Reservacion(
                        item['nombre_cliente'],
                        datetime.strptime(item['fecha_reserva'], '%Y-%m-%d'),
                        datetime.strptime(item['fecha_entrada'], '%Y-%m-%d'),
                        datetime.strptime(item['fecha_salida'], '%Y-%m-%d'),
                        int(item['num_habitacion']),
                        int(item['duracion_estadia']),
                        item['tipo_habitacion'],
                        item['preferencias_alimentarias'],
                        int(item['num_personas']),
                        item['contacto'],
                        float(item['precio_total']),
                        item['metodo_pago'],
                        item['notas_adicionales'],
                        item['estado_reservacion'],
                        item['hora_checkin_checkout'],
                        int(item['id_reservacion']),
                        item['correo_cliente']
                    )
                    self.reservaciones.append(reservacion)

#Ordenar segun criterios de ordenamiento dados por el usuario//metodo quicksort
    def ordenar_reservaciones(self, criterios):
        return 
#Ordenamiento Multiple segun criterios dados por el usuario        
    def ordenar_reservaciones_multiple(self, criterios):
        return
#Ordenamiento segun el precio total de forma ascendente o descendente(Solo de las reservaciones que caigan en el rango de las fechas que el usuario da)//metodo mergesort
    def ordenar_reservaciones_por_rango(self, fecha_inicio, fecha_fin, ascendente=True):
        print("precio_total")

#Ordenamiento segun las reservaciones que tenga el usuario //metodo Shellsort 
    def listar_clientes_por_reservaciones(self, ascendente=True):
        return

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
            if left[i] < right[j]:
                output.append(left[i])
                i += 1
            else:
                output.append(right[j])
                j += 1
        output.extend(left[i:])
        output.extend(right[j:])
        return output

manager = SistemaReservaciones()
manager.cargar_datos("datos.json")
manager.ordenar_reservaciones_por_rango