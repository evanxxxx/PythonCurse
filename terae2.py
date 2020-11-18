if __name__ == "__main__":
    b=[]
    a = input("Ingresa un saludo :")
    for i in a:
        if i == i.lower():
            b.append(i.upper()) 
        elif i == i.upper():
            b.append(i.lower())  
    print("" .join(b))        
        
             
        
