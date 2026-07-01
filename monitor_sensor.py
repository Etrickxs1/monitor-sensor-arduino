import serial
import time
import os
from datetime import datetime

arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)
arduino.flushInput()

print("=== Monitor de Potenciómetro con Alarma ===")
print("Gira la perilla — LED enciende al superar 50%")
print("Presiona Ctrl+C para detener\n")

# Verificamos si el archivo existe antes de entrar al ciclo
archivo_existe = os.path.exists('historial_sensor.csv')

# Creamos el encabezado si el archivo es nuevo
if not archivo_existe:
    with open('historial_sensor.csv', 'w', newline='') as archivo:
        archivo.write("timestamp,valor,porcentaje,estado\n")

while True:
    dato = arduino.readline().decode('utf-8').strip()
    
    if dato and dato.isdigit():
        valor = int(dato)
        porcentaje = (valor / 1023) * 100
        barras = int(porcentaje / 5)
        
        # Capturamos el momento exacto de la lectura
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Determinamos el estado
        estado = "ALARMA" if porcentaje > 50 else "Normal"
        
        print(f"Valor: {valor:4d} | Porcentaje: {porcentaje:5.1f}% | {'█' * barras}")
        
        # Guardamos en CSV
        with open('historial_sensor.csv', 'a', newline='') as archivo:
            archivo.write(f"{timestamp},{valor},{porcentaje:.1f},{estado}\n")
        
        if porcentaje > 50:
            arduino.write(b'1')
            time.sleep(0.08)
            respuesta = arduino.readline().decode('utf-8').strip()
            if respuesta:
                print(f"Arduino: {respuesta}")
            else:
                print("ADVERTENCIA: Arduino no respondió")
        else:
            arduino.write(b'0')
            time.sleep(0.08)
            respuesta = arduino.readline().decode('utf-8').strip()
            if respuesta:
                print(f"Arduino: {respuesta}")
            else:
                print("ADVERTENCIA: Arduino no respondió")

arduino.close()