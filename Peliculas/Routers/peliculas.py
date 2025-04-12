from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from Models import models, schemas
from dependencies import get_db

router = APIRouter()

@router.post("/peliculas/subir", response_model=schemas.MovieCreate, tags=['Peliculas CRUD'])
def subir_pelicula(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

@router.put("/pelicula/{movie_id}", response_model=schemas.MovieCreate, tags=['Peliculas CRUD'])
def actualizar_pelicula(movie_id: int, movie: schemas.MovieUpdate, db: Session = Depends(get_db)):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Pelicula no encontrada")

    for key, value in movie.dict(exclude_unset=True).items():
        setattr(db_movie, key, value)

    db.commit()
    db.refresh(db_movie)
    return db_movie

@router.delete("/pelicula/delete={movie_id}", tags=['Peliculas CRUD'])
def borrar_pelicula(movie_id: int, db: Session = Depends(get_db)):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Pelicula no encontrada")
    db.delete(db_movie)
    db.commit()
    return {"mensaje": "Pelicula eliminada exitosamente"}

@router.get("/movies/all", tags=['Peliculas CRUD'])
def mostrar_peliculas(db: Session = Depends(get_db)):
    return db.query(models.Movie).all()

@router.get("/movies/buscar={movie_id}", tags=['Peliculas CRUD'])
def buscar_pelicula(movie_id: int, db: Session = Depends(get_db)):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Pelicula no encontrada")
    return db_movie
