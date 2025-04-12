from pydantic import BaseModel, Field

class MovieCreate(BaseModel):
    title: str = Field(min_length=2)
    genre: str = Field(min_length=4)
    year: int = Field(ge=1000, le=9999)
    classification: str = Field(pattern="^[ABC]$")
