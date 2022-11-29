from fastapi import FastAPI
from routes.address_routes import address

app = FastAPI()

app.include_router(address)
