from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from requests import Request
from airtable_api import get_data_projet_affichage
from airtable_api import put_new_project
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Create_project(BaseModel):
    nom_du_projet: str
    description_du_projet: str
    besoins_actuels: str
    domaine_activite: str
    maturite_du_projet: str
    lieu_du_projet: str
    code_postal: str
    odd: List[str]
    matieres_entrantes: str
    coproduits: str


@app.get("/")
async def root():
    return {"message": "Hello world from FastAPI!"}


@app.post("/create-project/")
async def create_project(create_project: Create_project):
    put_new_project(create_project)
    return create_project


@app.get("/links-between-projects/")
async def links_between_projects():
    return JSONResponse(content=get_data_projet_affichage())
