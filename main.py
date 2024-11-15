import os
from nicegui import ui

port = int(os.environ.get("PORT", 8080))  # Obtén el puerto de Heroku o usa 8080 por defecto

def calcular_distancia(velocidad, tiempo):
    return velocidad * tiempo

def calcular_velocidad(distancia, tiempo):
    return distancia / tiempo

def calcular_tiempo(distancia, velocidad):
    return distancia / velocidad

def calcular():
    try:
        if opcion.value == 'Distancia':
            velocidad = float(velocidad_input.value)
            tiempo = float(tiempo_input.value)
            resultado = calcular_distancia(velocidad, tiempo)
            resultado_label.text = f"Distancia = {resultado:.2f} m"
        elif opcion.value == 'Velocidad':
            distancia = float(distancia_input.value)
            tiempo = float(tiempo_input.value)
            resultado = calcular_velocidad(distancia, tiempo)
            resultado_label.text = f"Velocidad = {resultado:.2f} m/s"
        elif opcion.value == 'Tiempo':
            distancia = float(distancia_input.value)
            velocidad = float(velocidad_input.value)
            resultado = calcular_tiempo(distancia, velocidad)
            resultado_label.text = f"Tiempo = {resultado:.2f} s"
    except ValueError:
        resultado_label.text = "Por favor, ingresa valores numéricos válidos."

with ui.column().classes('justify-center items-center w-full h-screen bg-gray-100'):
    ui.label("Calculadora de Movimiento Rectilíneo Uniforme (MRU)").classes('text-3xl font-bold mb-6 text-center')
    ui.label("Selecciona lo que deseas calcular:").classes('text-lg mb-2')
    opcion = ui.radio(['Distancia', 'Velocidad', 'Tiempo'], value='Distancia').classes('mb-4')
    distancia_input = ui.input(label="Distancia (m)").classes('my-2 w-1/3')
    velocidad_input = ui.input(label="Velocidad (m/s)").classes('my-2 w-1/3')
    tiempo_input = ui.input(label="Tiempo (s)").classes('my-2 w-1/3')
    ui.button("Calcular", on_click=calcular).classes(
        'my-4 bg-blue-500 text-white font-bold px-4 py-2 rounded shadow hover:bg-blue-600')
    resultado_label = ui.label().classes('text-xl font-semibold mt-6 text-center')

ui.run(port=port)  # Asegúrate de que la app escuche en el puerto correcto
