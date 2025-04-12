from fastapi import FastAPI
from Routers import peliculas
from DB.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(peliculas.router)