from fastapi import FastAPI

app = FastAPI()

BANDS = [
    {'id': 1, 'name': 'The Kinks', 'genre': 'Rock'},
    {'id': 2, 'name': 'Aphex Twin', 'genre': 'Electronic'},
    {'id': 3, 'name': 'Slowdive', 'genre': 'Shoegaze'},
    {'id': 4, 'name': 'Wu-Tang Clan', 'genre': 'Hip-Hop'},    
]

@app.get('/')
async def index() -> dict[str, str]:
    return {'Hello, World!'}

@app.get('/about')
async def about() -> str:
    return  'An exceptional company'