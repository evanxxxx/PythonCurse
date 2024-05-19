import uuid
from datetime import datetime
from fastapi import FastAPI, HTTPException, status
from sqlmodel import Field, SQLModel, create_engine, Session, select



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

@app.get("/users1/{user_id}")
def search_user_api(user_id :int, user: User):
   with Session(engine) as session:
        db_user= session.get(User, user.user_id == user_id)
        
        if not db_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Error, The user was not found.")      
        else:   
            return user
    
@app.get("/users/{user_id}")
def search_user_api(user_id :int):
   with Session(engine) as session:
        query = select(User).where(User.user_id == user_id)
        search = session.exec(query).first()
        if not search:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Error, The user was not found.")      
        else:   
            return search


            
        
@app.get("/health")
def root()-> dict:
    return {
        "status" : "Up"
    }