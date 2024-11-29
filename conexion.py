from ftplib import FTP
ftp_server = 'localhost'
username = input("Ingresa el nombre de usuario: ")
password = input("Ingresa la contraseña: ")

try:
    # Conectar al servidor FTP
    ftp = FTP(ftp_server)
    ftp.login(user=username, passwd=password)

    print("Conexión exitosa!")

    ftp.retrlines('LIST')

    ftp.quit()
except Exception as e:
    print(f"Ocurrió un error: {e}")
