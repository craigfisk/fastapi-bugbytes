# pydantic models

from datetime import date
from enum import Enum
from pydantic import BaseModel, validator, model_validator
from sqlmodel import SQLModel, Field, Relationship

class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop'

class GenreChoices(Enum):
    ROCK = 'Rock'
    ELECTRONIC = 'Electronic'
    METAL = 'Metal'
    HIP_HOP = 'Hip-Hop'

class AlbumBase(SQLModel): 
    title: str
    release_date: date
    band_id: int | None = Field(foreign_key="band.id")

class Album(AlbumBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    band: "Band" = Relationship(back_populates="albums")
  
class BandBase(SQLModel):
    name: str
    genre: GenreChoices

class BandCreate(BandBase):
    albums: list[AlbumBase] | None = None  # Default is an empty list; also 'Album' is Album in BugBytes #3@14:04
    @model_validator(mode='before')
    def validate_genre(cls, data):
        genre_str = data.get('genre')
        if genre_str:
            genre_str = genre_str.replace('-', '_').upper()
            try:
                data['genre'] = GenreChoices[genre_str]
            except KeyError:
                raise ValueError(f"Invalid genre: {data.get('genre')}")
        return data

class Band(BandBase, table =True):
    id: int = Field(default=None, primary_key=True)
    albums: list[Album] = Relationship(back_populates="band")

