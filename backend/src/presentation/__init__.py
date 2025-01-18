from fastapi import APIRouter
from .productRouter import router as ProductsRouter
from .orderRouter import router as OrderRouter

router = APIRouter(prefix="/api/v1")
router.include_router(ProductsRouter)
router.include_router(OrderRouter)
