from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List
from api.models import Product
from services.db import get_session

router = APIRouter(prefix="/catalog", tags=["Catalog"])

@router.get("/", response_model=List[Product])
def all_products(db: Session = Depends(get_session)):
    return db.exec(select(Product)).all()
