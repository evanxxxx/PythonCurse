if __name__ == "__main__":
    renta = int(input("Ingresa tu renta anual: "))
    if renta < 10000:
        print("El iva correspondiente es el 5%")
    elif renta >= 10000 and renta < 20000:
        print("El iva correspondiente es el 15%")
    elif renta >= 20000 and renta < 35000:
        print("El iva correspondiente es el 20%")
    elif renta >= 35000 and renta < 60000:
        print("El iva correspondiente es el 30%")
    elif renta >= 60000:
        print("El iva correspondiente es el 45%")