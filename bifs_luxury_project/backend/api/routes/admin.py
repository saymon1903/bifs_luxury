from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlmodel import Session, select
from api.models import Product
from api.auth import get_current
from services.db import get_session
import uuid, shutil, os

router = APIRouter(prefix="/admin", tags=["Admin"])

UPLOAD_DIR = "static/products"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/product")
async def add_product(title: str, price: float, description: str,
                      stock: int,
                      file: UploadFile = File(...),
                      user=Depends(get_current),
                      db: Session = Depends(get_session)):
    if not user.is_admin:
        raise HTTPException(403)
    fn = f"{uuid.uuid4()}{os.path.splitext(file.filename)[1]}"
    dest = os.path.join(UPLOAD_DIR, fn)
    with open(dest, "wb") as out:
        shutil.copyfileobj(file.file, out)
    prod = Product(title=title, price=price, description=description,
                   stock=stock, thumbnail=f"/{dest}", slug=title.lower().replace(" ", "-"))
    db.add(prod); db.commit(); db.refresh(prod)
    return prod
