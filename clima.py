import urllib.request
import json
import csv
import datetime
import os

# 1. Configuración 
API_KEY = "c8fb29956631fe51156dd54569038b53"
LAT = "-0.2299"
LON = "-78.5249"
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"

# Usamos la carpeta personal para evitar errores de permisos
CSV_FILE = os.path.expanduser("~/clima-quito-hoy.csv")

def obtener_clima():
    try:
        # Hacemos la consulta al API
        respuesta = urllib.request.urlopen(URL)
        datos = json.loads(respuesta.read().decode('utf-8'))
        
        # Extraemos la temperatura y humedad
        temp = datos['main']['temp']
        humedad = datos['main']['humidity']
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Verificamos si el archivo ya existe para ponerle los encabezados
        archivo_existe = os.path.isfile(CSV_FILE)
        
        # Escribimos en el archivo CSV ('a' es de append, para no borrar lo anterior)
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not archivo_existe:
                writer.writerow(['Fecha_Hora', 'Temperatura_C', 'Humedad_%'])
            writer.writerow([fecha_hora, temp, humedad])
            
        print(f"Éxito: Datos guardados a las {fecha_hora}")
        
    except Exception as e:
        print(f"Error al conectar con el API: {e}")

obtener_clima()
