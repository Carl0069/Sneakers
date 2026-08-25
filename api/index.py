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
  },
  {
    "id": 6,
    "brand": "Nike",
    "model": "Air Yeezy 2",
    "colorway": "Red October",
    "release_year": 2014,
    "price": 250,
    "description": "A highly sought-after Nike basketball-inspired sneaker known for its bold design."
  },
  {
    "id": 7,
    "brand": "Nike",
    "model": "Air Jordan 4",
    "colorway": "White Cement",
    "release_year": 1989,
    "price": 210,
    "description": "A classic basketball silhouette featuring the iconic cement print detailing."
  },
  {
    "id": 8,
    "brand": "Nike",
    "model": "Air Force 1",
    "colorway": "Triple White",
    "release_year": 1982,
    "price": 120,
    "description": "A timeless all-white sneaker known for its clean design and versatile style."
  },
  {
    "id": 9,
    "brand": "Adidas",
    "model": "Samba OG",
    "colorway": "Cloud White / Core Black",
    "release_year": 1950,
    "price": 100,
    "description": "A classic low-profile sneaker that blends its soccer heritage with modern streetwear."
  },
  {
    "id": 10,
    "brand": "Nike",
    "model": "Dunk Low",
    "colorway": "Panda",
    "release_year": 1985,
    "price": 115,
    "description": "A popular low-top sneaker featuring a simple black and white color scheme."
  },
  {
    "id": 11,
    "brand": "Adidas",
    "model": "Gazelle",
    "colorway": "Bold Blue / White",
    "release_year": 1966,
    "price": 100,
    "description": "A retro suede sneaker with a classic silhouette and signature three stripes."
  },
  {
    "id": 12,
    "brand": "New Balance",
    "model": "574",
    "colorway": "Grey / White",
    "release_year": 1988,
    "price": 90,
    "description": "A versatile lifestyle sneaker recognized for its classic grey styling and comfort."
  },
  {
    "id": 13,
    "brand": "Vans",
    "model": "Old Skool",
    "colorway": "Black / White",
    "release_year": 1977,
    "price": 75,
    "description": "An iconic skate shoe featuring Vans' signature side stripe."
  },
  {
    "id": 14,
    "brand": "Puma",
    "model": "Suede Classic",
    "colorway": "Black / White",
    "release_year": 1968,
    "price": 80,
    "description": "A legendary suede sneaker with a simple design rooted in street culture."
  },
  {
    "id": 15,
    "brand": "Reebok",
    "model": "Club C 85",
    "colorway": "Chalk / Green",
    "release_year": 1985,
    "price": 85,
    "description": "A clean vintage tennis-inspired sneaker with a minimalist leather upper."
  },
  {
    "id": 16,
    "brand": "ASICS",
    "model": "Gel-Kayano 14",
    "colorway": "Cream / Black",
    "release_year": 2008,
    "price": 150,
    "description": "A retro running sneaker combining early-2000s styling with modern comfort."
  },
  {
    "id": 17,
    "brand": "ASICS",
    "model": "Gel-Lyte III",
    "colorway": "White / Blue",
    "release_year": 1990,
    "price": 120,
    "description": "A classic running-inspired sneaker known for its split tongue design."
  },
  {
    "id": 18,
    "brand": "Hoka",
    "model": "Clifton 9",
    "colorway": "White / Black",
    "release_year": 2023,
    "price": 145,
    "description": "A lightweight running shoe designed for a soft and responsive ride."
  },
  {
    "id": 19,
    "brand": "Adidas",
    "model": "Superstar",
    "colorway": "White / Black",
    "release_year": 1970,
    "price": 100,
    "description": "A classic shell-toe sneaker that became a staple of streetwear and pop culture."
  },
  {
    "id": 20,
    "brand": "Nike",
    "model": "Air Max 90",
    "colorway": "Infrared",
    "release_year": 1990,
    "price": 130,
    "description": "A legendary Air Max silhouette famous for its bold infrared accents and visible Air unit."
  }
]

# HOME
@app.get("/api")
def home():
    return {
        "message": "Welcome to the Simple Sneaker API!",
        "endpoints": [
            "/api/sneakers",
            "/api/sneakers/{id}",
            "/api/sneakers/search"
        ]
    }


# GET ALL SNEAKERS
@app.get("/api/sneakers")
def get_sneakers():
    return {
        "count": len(sneakers),
        "sneakers": sneakers
    }


# GET ONE SNEAKER
@app.get("/api/sneakers/{sneaker_id}")
def get_sneaker(sneaker_id: int):
    for sneaker in sneakers:
        if sneaker["id"] == sneaker_id:
            return sneaker

    raise HTTPException(
        status_code=404,
        detail="Sneaker not found."
    )


# SEARCH SNEAKERS
@app.get("/api/sneakers/search")
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
