from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
# OAuth2PasswordBearer Se encarga de gestionar la autenticacion usuario y pass
# OAuth2PasswordRequestForm La forma en como se va a enviar a nuestro backend los criterios de autenticacion
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()
# tokenUrl para indicar cual es la Url que se va a encargar de la autenticacion 
oauth2 = OAuth2PasswordBearer(tokenUrl="login")



class User(BaseModel):
    username : str
    name : str
    email : str
    disable : bool

class UserDB(User):
    password : str

users_db = {
    "evan" : {
        "username" : "evan",
        "name" : "Evan Navarro",
        "email" : "evan.navarro@gmail.com",
        "disable" : False,
        "password" : "123456"
    },
        "carlos" : {
        "username" : "carlos",
        "name" : "Carlos Becerro",
        "email" : "carlos.becerro@gmail.com",
        "disable" : True,
        "password" : "654321"
    }
}

def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])
    
def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])

#vamos a autenticar, como vamos a enviar y a recibir datos se utiliza un POST   

# vamos a capturar los datos gracias a OAuth2PasswordRequestForm mediante un formulario y se declaran los parametros de la funcion
# vamos a decir que el form por defecto va a venir de depends (nos ayuda a saber si nos autenticamos o no a que podemos acceder de acuerdo a los criterios que se declararon)
# (va a recibir datos pero no depende d enadie)
@app.post("/login")
async def login(form : OAuth2PasswordRequestForm = Depends()): 
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="el usuario no es correcto")
    

    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="la contraseña no es correcto")
    # Si el usuario ha sido autenticado por estandar devuelve un access_token y el tipo bearer
    return {"access_token" : user.username ,"token_type" : "bearer"}



async def current_user(token:str = Depends(oauth2)):
    user =  search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Credenciales invalidas", 
                            headers={"www-autenticate": "bearer"}) 
    if user.disable:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Usuario Inactivo") 
    return user       

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user