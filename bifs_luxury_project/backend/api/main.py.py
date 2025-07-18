from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.catalog import router as catalog_router
from api.routes.admin import router as admin_router
from services.db import init_db

app = FastAPI(title="BIFS Luxury API", version="2.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"],
                   allow_headers=["*"])
app.include_router(catalog_router)
app.include_router(admin_router)

@app.on_event("startup")
def start():
    init_db()

@app.get("/")
def root():
    return {"msg": "BIFS Luxury – API live"}
