from fastapi import FastAPI
from routers import validMain

app = FastAPI()

app.include_router(validMain.router)