def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return print(full_name)

def get_data():
    global first_name, last_name
    first_name = input ("Ingresa tu nombre : ")
    last_name = input ("Ingresa tu apellido : ")
    return first_name, last_name

get_data()
get_full_name(first_name, last_name)