if __name__ == "__main__":
    edad = input("Ingresa tu edad: ")
    salario = input("Ingresa tu salario: ")
    if int(edad) > 16 and int(salario) > 1000:
        print("Tienes que tributar")
    else:
        print("No tienes que tributar")