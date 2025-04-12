from pydantic import BaseModel, Field, validator
from typing import Optional
import re

class MovieCreate(BaseModel):
    title: str = Field(..., min_length=2, description="Debe tener al menos 2 caracteres")
    genre: str = Field(..., min_length=4, description="Debe tener al menos 4 letras")
    year: int = Field(..., description="Debe tener 4 dígitos")
    classification: str = Field(..., min_length=1, max_length=1, description="Debe ser un solo carácter: A, B o C")

    @validator("title")
    def validate_title(cls, v):
        if len(v.strip()) < 2:
            raise ValueError("El título debe tener al menos 2 caracteres")
        if not re.match(r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ :,\-'\"]+$", v):
            raise ValueError("El título solo puede contener letras, números, espacios y los caracteres : , - ' \"")
        return v

    @validator("genre")
    def validate_genre(cls, v):
        if len(v.strip()) < 4:
            raise ValueError("El género debe tener al menos 4 letras")
        if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", v):
            raise ValueError("El género solo debe contener letras")
        return v

    @validator("year")
    def validate_year(cls, v):
        if v < 1000 or v > 9999:
            raise ValueError("El año debe tener 4 dígitos")
        return v

    @validator("classification")
    def validate_classification(cls, v):
        if v.upper() not in ["A", "B", "C"]:
            raise ValueError("Clasificación inválida. Solo se permite A, B o C")
        return v.upper()

class MovieUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=2, description="Debe tener al menos 2 caracteres")
    genre: Optional[str] = Field(None, min_length=4, description="Debe tener al menos 4 letras")
    year: Optional[int] = Field(None, description="Debe tener 4 dígitos")
    classification: Optional[str] = Field(None, min_length=1, max_length=1, description="Debe ser un solo carácter: A, B o C")

    @validator("title")
    def validate_title(cls, v):
        if len(v.strip()) < 2:
            raise ValueError("El título debe tener al menos 2 caracteres")
        if not re.match(r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ :,\-'\"]+$", v):
            raise ValueError("El título solo puede contener letras, números, espacios y los caracteres : , - ' \"")
        return v

    @validator("genre")
    def validate_genre(cls, v):
        if len(v.strip()) < 4:
            raise ValueError("El género debe tener al menos 4 letras")
        if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", v):
            raise ValueError("El género solo debe contener letras")
        return v

    @validator("year")
    def validate_year(cls, v):
        if v < 1000 or v > 9999:
            raise ValueError("El año debe tener 4 dígitos")
        return v

    @validator("classification")
    def validate_classification(cls, v):
        if v.upper() not in ["A", "B", "C"]:
            raise ValueError("Clasificación inválida. Solo se permite A, B o C")
        return v.upper()