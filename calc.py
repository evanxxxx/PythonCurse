def suma(a: int, b: int)-> int:
    '''
    regresa la suma de dos numeros
    '''
    return a + b

def resta(a: int, b: int)-> int:
    '''
    regresa la resta de dos numeros
    '''
    return a - b

def multiplicacion(a: int, b: int)-> int:
    '''
    regresa la multiplicacion de dos numeros
    '''
    return a * b

def division(numerador: float, denominador: float)-> float:
    '''
    regresa la division de dos numeros
    '''
    if denominador == 0.0:
        return "El demonimador no puede ser cero"
    else:     
        return numerador / denominador

if __name__ == "__main__":
    print("El resultado de la suma es: ", suma(2,2))
    print("El resultado de la resta es: ", resta(3,5))
    print("El resultado de la multiplicacion es: ", multiplicacion(4,4))
    print("El resultado de la division es: ", division(5,0))
  