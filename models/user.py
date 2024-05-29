from pydantic import BaseModel

# model
class User(BaseModel):
    name : str
    email : str
    password : str 
    

