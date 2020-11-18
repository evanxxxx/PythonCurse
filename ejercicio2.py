if __name__ == "__main__":
    
    password_uno = input("Ingresa la contraseña: ")
    password_dos = input("Ingresa nuevamente la contraseña: ")

    if password_uno.upper() == password_dos.upper():
        print("Las contraseñas son iguales")
    else:
        print("La contraseña esta mal")

