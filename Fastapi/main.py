from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

class Role(BaseModel):
    role_id: int
    role_name: str
    created_ad: datetime
	desccription: str
	created_at: datetime
	updated_at: datetime
	deleted: bool
	deleted_at: datetime
    

