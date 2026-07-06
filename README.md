# Monitor de Sensor con Control de Alarma
Sistema de monitoreo en tiempo real con Arduino y Python que lee datos 
de un sensor analógico, evalúa umbrales de alarma y controla un actuador 
físico automáticamente. Registra historial completo en formato CSV.

## Descripción
Este proyecto implementa un lazo de control cerrado básico:
- **Sensor:** Potenciómetro de 5K como sensor analógico simulando variables de proceso
- **Microcontrolador:** Arduino Uno (compatible Geekcreít) leyendo señal analógica en A0
- **Control:** Python evalúa el valor en tiempo real y decide activar o desactivar la alarma
- **Actuador:** LED conectado al pin 13 como indicador de alarma
- **Registro:** Historial automático en CSV con timestamp, valor, porcentaje y estado

## Tecnologías
- Python 3.13
- Arduino IDE 2.x / C++
- Librería pyserial para comunicación serial
- Comunicación serial a 9600 baudios

## Hardware requerido
- Arduino Uno o compatible
- Potenciómetro 5K ohms
- LED (cualquier color)
- Resistencia 330 ohms
- Protoboard y cables jumper
- Cable USB tipo A a tipo B

## Cómo ejecutar
1. Conecta el circuito según el esquema: potenciómetro en A0, LED en pin 13
2. Sube `sensor_arduino.ino` al Arduino con Arduino IDE
3. Instala la dependencia de Python:
   pip install pyserial
4. Ejecuta el monitor:
   python monitor_sensor.py
5. Gira el potenciómetro — el LED enciende automáticamente al superar 50%
6. Presiona Ctrl+C para detener y revisar el historial en `historial_sensor.csv`

## Ejemplo de salida
```
Valor:  523 | Porcentaje:  51.1% | ██████████
Arduino: LED encendido
Valor:  489 | Porcentaje:  47.8% | █████████
Arduino: LED apagado
```

## Registro CSV generado automáticamente
timestamp,valor,porcentaje,estado
2026-06-09 16:05:47,365,35.7,Normal
2026-06-09 16:05:48,521,50.9,ALARMA
2026-06-09 16:05:49,1002,97.9,ALARMA

## Autor
Erick Pecero — Ingeniero Electrónico  
Especialización en Automatización Industrial  
GitHub: github.com/Etrickxs1