if __name__ == "__main__":
    nombre = input("Cual es tu nombre: ").lower()
    letra = nombre[0]
    sexo = input("Cual es tu sexo: ").lower()

    grupo_mujeres = ["a","b","c","d","e","f","g","h","i","j","k","l"]
    grupo_hombres = ["o","p","q","r","s","t","u","v","w","x","y","z"]

    if sexo == "mujer" and letra in grupo_mujeres:
        print("Perteneces al grupo A")
    elif sexo == "hombre" and letra in grupo_hombres:
        print("Perteneces al grupo A")
    else: 
        print("Perteneses al grupo B")