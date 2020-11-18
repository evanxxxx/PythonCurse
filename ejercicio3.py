if __name__ == "__main__":
    import math
    divisor = input("Ingresa el divisor: ")
    dividendo = input("ingresa el dividendo: ")
    
    if int(divisor) == 0:
        print("Error")
    else:
        result = int(divisor)/int(dividendo)   
        print("El resultado es: ",result)