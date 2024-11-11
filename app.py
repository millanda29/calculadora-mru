from nicegui import ui


# Función para calcular distancia en MRU
def calcular_distancia(velocidad, tiempo):
    return velocidad * tiempo


# Función para calcular velocidad en MRU
def calcular_velocidad(distancia, tiempo):
    return distancia / tiempo


# Función para calcular tiempo en MRU
def calcular_tiempo(distancia, velocidad):
    return distancia / velocidad


# Función principal para el cálculo basado en la opción seleccionada
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


# Interfaz gráfica de la aplicación
with ui.column().classes('justify-center items-center w-full h-screen bg-gray-100'):

    # Título de la aplicación
    ui.label("Calculadora de Movimiento Rectilíneo Uniforme (MRU)").classes('text-3xl font-bold mb-6 text-center')

    # Opciones para calcular Distancia, Velocidad o Tiempo
    ui.label("Selecciona lo que deseas calcular:").classes('text-lg mb-2')
    opcion = ui.radio(['Distancia', 'Velocidad', 'Tiempo'], value='Distancia').classes('mb-4')

    # Inputs para ingresar distancia, velocidad y tiempo
    distancia_input = ui.input(label="Distancia (m)").classes('my-2 w-1/3')
    velocidad_input = ui.input(label="Velocidad (m/s)").classes('my-2 w-1/3')
    tiempo_input = ui.input(label="Tiempo (s)").classes('my-2 w-1/3')

    # Botón de cálculo
    ui.button("Calcular", on_click=calcular).classes(
        'my-4 bg-blue-500 text-white font-bold px-4 py-2 rounded shadow hover:bg-blue-600')

    # Área para mostrar el resultado
    resultado_label = ui.label().classes('text-xl font-semibold mt-6 text-center')

# Ejecutar la aplicación
ui.run()