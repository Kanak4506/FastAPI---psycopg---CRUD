from fastapi import APIRouter
from app.schemas.product_schema import ProductCreate, ProductUpdate, ProductPatch
from app.services.product_service import (
    create_product,
    get_all_products,
    get_product,
    update_product,
    delete_product,
    patch_product,
)

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/")
def add_product(product: ProductCreate):
    return create_product(product)


@router.get("/")
def fetch_products():
    return get_all_products()


@router.get("/{id}")
def fetch_product(id: int):
    return get_product(id)


@router.put("/{id}")
def edit_product(id: int, product: ProductUpdate):
    return update_product(id, product)


@router.delete("/{id}")
def remove_product(id: int):
    return delete_product(id)


@router.patch("/{id}")
def update_partial_product(id: int, product: ProductPatch):
    return patch_product(id, product)
