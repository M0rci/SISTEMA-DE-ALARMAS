def sistema_alerta_meteorologica():
    print("== MONITOREO CLIMÁTICO PARA PREVENCIÓN DE TORMENTAS ==")

    continuar = True
    while continuar:
        print("\nSeleccione una opción:")
        print("1. Ingresar datos manualmente")
        print("2. Usar datos de simulación")

        opcion = input("Opción (1/2): ").strip()
        if opcion == "2":
            temperatura = 15
            presion = 1002
            humedad = 65
            viento = 15
            print("\nUsando datos de simulación...")
        elif opcion == "1":
            try:
                temperatura = float(input("Ingrese temperatura (°C): "))
                presion = float(input("Ingrese presión atmosférica (hPa): "))
                humedad = float(input("Ingrese humedad relativa (%): "))
                viento = float(input("Ingrese velocidad del viento (km/h): "))
            except ValueError:
                print("⚠️ Entrada inválida. Por favor, solo ingrese números.")
                continue
        else:
            print("⚠️ Opción inválida.")
            continue

        print("\n--- Análisis del clima actual ---")
        print(f"Temperatura: {temperatura} °C")
        print(f"Presión atmosférica: {presion} hPa")
        print(f"Humedad: {humedad} %")
        print(f"Velocidad del viento: {viento} km/h")

        condiciones_alerta = (
            10 <= temperatura <= 25 and
            1000 <= presion <= 1010 and
            60 <= humedad <= 100 and
            5 <= viento <= 15
        )

        if condiciones_alerta:
            print("\n⚠️ ALERTA METEOROLÓGICA: Posible tormenta eléctrica detectada.")
        else:
            print("\n✅ Condiciones estables. No se detectan alertas.")

        repetir = input("\n¿Desea analizar otro conjunto de datos? (s/n): ").strip().lower()
        if repetir != 's':
            continuar = False
            print("Finalizando monitoreo. Gracias por usar el sistema.")

sistema_alerta_meteorologica()
