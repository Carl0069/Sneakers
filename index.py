from fastapi import FastAPI, HTTPException, Header, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Simple Sneaker API",
    description="A beginner-friendly REST API containing information about sneakers.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SNEAKER DATA
sneakers = [
    {
        "id": 1,
        "brand": "Nike",
        "model": "Air Jordan 1 High OG",
        "colorway": "Chicago",
        "release_year": 1985,
        "price": 180,
        "description": "The iconic high-top basketball sneaker that launched the Jordan line."
    },
    {
        "id": 2,
        "brand": "Adidas",
        "model": "Samba Classic",
        "colorway": "Cloud White / Core Black",
        "release_year": 1950,
        "price": 100,
        "description": "A legendary indoor soccer shoe turned street-style staple."
    },
    {
        "id": 3,
        "brand": "New Balance",
        "model": "550",
        "colorway": "White / Green",
        "release_year": 1989,
        "price": 110,
        "description": "A retro low-profile basketball design with clean vintage vibes."
    },
    {
        "id": 4,
        "brand": "Nike",
        "model": "Air Max 1",
        "colorway": "University Red",
        "release_year": 1987,
        "price": 140,
        "description": "The first sneaker to showcase visible Air cushioning technology."
    },
    {
        "id": 5,
        "brand": "Converse",
        "model": "Chuck 70 High",
        "colorway": "Black / Egret",
        "release_year": 1970,
        "price": 90,
        "description": "A premium canvas sneaker built with vintage stitching and extra cushioning."
    }
]

# HOME
@app.get("/")
def home():
    return {
        "message": "Welcome to the Simple Sneaker API!",
        "endpoints": [
            "/sneakers",
            "/sneakers/{id}",
            "/sneakers/search"
        ]
    }

# GET ALL SNEAKERS
@app.get("/sneakers")
def get_sneakers():
    return {
        "count": len(sneakers),
        "sneakers": sneakers
    }

# GET ONE SNEAKER
@app.get("/sneakers/{sneaker_id}")
def get_sneaker(sneaker_id: int):
    for sneaker in sneakers:
        if sneaker["id"] == sneaker_id:
            return sneaker

    raise HTTPException(
        status_code=404,
        detail="Sneaker not found."
    )

# SEARCH SNEAKERS
@app.get("/sneakers/search")
def search_sneakers(q: str = Query(..., min_length=1)):
    q = q.lower()
    results = []
    for sneaker in sneakers:
        searchable_text = (
            f"{sneaker['brand']} "
            f"{sneaker['model']} "
            f"{sneaker['colorway']} "
            f"{sneaker['release_year']}"
        ).lower()

        if q in searchable_text:
            results.append(sneaker)

    return {
        "query": q,
        "count": len(results),
        "results": results
    }