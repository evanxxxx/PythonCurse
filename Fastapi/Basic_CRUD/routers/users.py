from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

router= APIRouter()
#app = FastAPI()


class User(BaseModel):
    id : int
    name : str
    edad : int 

users_list = [
    User(id = 1, name = "Evan", edad = "33"),
    User(id = 2, name = "Jose", edad = "35"),
    User(id = 3, name = "Omar", edad = "38"),
        ]

@router.get("/usersjson")
async def usersjson():
    return [
        {"name" : "Evan", "edad" : "33"},
        {"name" : "Jose", "edad" : "35"},
        {"name" : "Omar", "edad" : "38"},
            ]

@router.get("/users")
async def users():
    return users_list
# Path
@router.get("/user/{id}")
async def user(id : int):
    return search_user(id)

    #users = filter(lambda user : user.id==id, users_list)
    #try:
    #    return list(users)[0]    
    #except: 
    #    return {"error" : "no se ha encontrado el usuario"}

# Query   
@router.get("/userquery/")
async def user(id : int):
    return search_user(id)

    #users = filter(lambda user : user.id==id, users_list)
    #try:
    #    return list(users)[0]    
    #except: 
    #    return {"error" : "no se ha encontrado el usuario"}
    
def search_user(id : int):
    users = filter(lambda user : user.id==id, users_list)
    try:
        return list(users)[0]   
    except: 
        return {"error" : "no se ha encontrado el usuario"}
    
@router.post("/user/", response_model=User ,status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="el usuario ya existe")

    else:
        users_list.append(user)
        return user
"""    
@app.delete("/user/") #opcion 1
async def user(user:User):
    if type(search_user(user.id)) == User:
        users_list.remove(user)
        return user
    else:
        return {"error" : "el usuario no existe"}
"""
@router.delete("/user/{id}")
async def user(id: int):

    found = False
    for index,item in enumerate(users_list):
        if item.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error" : "no se ha eliminado el usuario"}



@router.put("/user/")
async def user(user:User):

    found= False

    for index,item in enumerate(users_list):
        if item.id == user.id:
            users_list[index] = user 
            found = True
    if not found:
        return {"error" : "el usuario no existe"}
    else:
        return user


