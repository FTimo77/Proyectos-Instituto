def calcular_promedio():
    calificaciones = []
    while True:
        calificacion = float(input("Ingrese una calificación (-1 para terminar): "))
        if calificacion == -1:
            break
        calificaciones.append(calificacion)
    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        return promedio
    return 0

promedio = calcular_promedio()
print(f"El promedio de las calificaciones es: {promedio:.2f}")
