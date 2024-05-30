import uuid
from datetime import datetime
from fastapi import FastAPI, HTTPException, status
from sqlmodel import Field, SQLModel, create_engine, Session


app = FastAPI()

database_url = "mysql+mysqlconnector://root:@localhost/meraki"
engine = create_engine(database_url)


class Role(SQLModel, table=True):
    """
    This Model Role represents a role assigned to a User Model into the database.
    """
    role_id: int = Field(default=None, primary_key=True)
    role_name: str
    description: str | None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = None
    deleted: bool = False
    deleted_at: datetime | None = None

class User(SQLModel, table=True):
    """ 
    This Model User represents a User into the database.
    """
    user_id: int = Field(default=None, primary_key=True)
    username: str
    password: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = None
    deleted: bool = False
    deleted_at: datetime | None = None

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/users/")
def create_user_api(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        db_user = session.get(User, user.user_id)
        if not db_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Error, The user was not found.")
    return user

@app.put("/users/{user_id}")
def update_user_api(user_id:int, user:User):
    with Session(engine) as session: 
        
        db_user = session.query(User).filter(User.user_id == user_id).first()
        
        for field, value in user.model_dump().items():
            if hasattr(db_user, field):
                setattr(db_user, field, value)
            
            db_user.user_id = user_id
            db_user.updated_at = datetime.now()
            
            session.commit()
            return {"message": "Usuario actualizado correctamente"}

    
@app.delete("/users/{user_id}")
def delet_user_api(user_id:int, user:User):
    with Session(engine) as session:
        db_user = session.get(User, user_id)     
        user.user_id = user_id
        user.deleted = True
        user.deleted_at = datetime.now()
        for key, value in user.model_dump().items():
                if hasattr(db_user, key):
                    setattr(db_user, key, value)
        session.commit()
        db_user = session.get(User, user_id)  
        return db_user
        
@app.get("/users/{user_id}")
def search_user_api(user_id:int):
    with Session(engine) as session:       
        db_user = session.query(User).filter(User.user_id == user_id).first()
        if db_user.deleted == False:
            return db_user
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Error, The user was not found.")   
            
@app.get("/health")
def root()-> dict:
    return {
        "status" : "Up"
    }