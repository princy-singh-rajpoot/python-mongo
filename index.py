from fastapi import FastAPI
from routes.vendor import vendor 

app= FastAPI()
app.include_router(vendor)