def obtener_calificacion_letra(calificacion):
    if 90 <= calificacion <= 100:
        return "A"
    elif 80 <= calificacion <= 89:
        return "B"
    elif 70 <= calificacion <= 79:
        return "C"
    elif 60 <= calificacion <= 69:
        return "D"
    elif 0 <= calificacion < 60:
        return "F"
    else:
        return "Calificación inválida"

def main():
    try:
        calificacion = float(input("Ingresa tu calificación numérica (0-100): "))
        letra = obtener_calificacion_letra(calificacion)
        print(f"Tu calificación es: {letra}")
    except ValueError:
        print("Por favor, ingresa un valor numérico válido.")

if __name__ == "__main__":
    main()
