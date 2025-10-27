# pydantic schemas
from datetime import date
from enum import Enum
from pydantic import BaseModel, validator, model_validator

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

class Album(BaseModel): 
    title: str
    release_date: date

class BandBase(BaseModel):
    name: str
    genre: GenreChoices
    albums: list[Album] = []   # Default is an empty list; also 'Album' is Album in BugBytes #3@14:04

class BandCreate(BandBase):
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

class BandWithID(BandBase):
    id: int

