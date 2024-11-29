def validar_acceso(usuario_correcto, contrasena_correcta):
    intentos = 3  # Número máximo de intentos permitidos

    while intentos > 0:
        # Solicitar datos al usuario
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        # Validar credenciales
        if usuario == usuario_correcto and contrasena == contrasena_correcta:
            print(f"Bienvenido, {usuario}.")
            return True
        else:
            intentos -= 1
            print(f"Usuario o contraseña incorrectos. Te quedan {intentos} intento(s).")

    print("Acceso bloqueado. Contacta al administrador.")
    return False

def main():
    # Credenciales correctas
    usuario_correcto = "admin"
    contrasena_correcta = "1234"

    validar_acceso(usuario_correcto, contrasena_correcta)

if __name__ == "__main__":
    main()
