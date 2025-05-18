# Parámetros meteorológicos actuales
temperatura = 20
presion = 1000
humedad = 87
viento = 10

# Configuración de alertas con nivel de severidad
alertas = [
    {
        "nombre": "ALERTA DE TORMENTA ELECTRICA",
        "nivel": "ROJA",
        "condiciones": [
            20 <= temperatura <= 30,
            1000 <= presion <= 1010,
            80 <= humedad <= 90,
            1 <= viento <= 40
        ]
    },
    {
        "nombre": "ALERTA DE VIENTOS FUERTES",
        "nivel": "NARANJA",
        "condiciones": [
            5 <= temperatura <= 30,
            616 <= presion <= 800,
            40 <= humedad <= 90,
            30 <= viento <= 100
        ]
    },
    {
        "nombre": "ALERTA DE LLUVIAS",
        "nivel": "AMARILLA",
        "condiciones": [
            5 <= temperatura <= 25,
            616 <= presion <= 1000,
            80 <= humedad <= 100,
            1 <= viento <= 25
        ]
    },
    {
        "nombre": "DÍA SOLEADO",
        "nivel": "VERDE",
        "condiciones": [
            20 <= temperatura <= 35,
            616 <= presion <= 800,
            15 <= humedad <= 60,
            1 <= viento <= 20
        ]
    }
]

# Evaluación de alertas activadas
alertas_activadas = []
for alerta in alertas:
    if all(alerta["condiciones"]):
        alertas_activadas.append((alerta["nombre"], alerta["nivel"]))

# Salida del sistema
print("=== SISTEMA DE ALERTAS ===")
if alertas_activadas:
    print("Estado:")
    for nombre, nivel in alertas_activadas:
        print(f"- {nombre} (Nivel: {nivel})")
else:
    print("SIN ALERTAS")
print("=========================")
