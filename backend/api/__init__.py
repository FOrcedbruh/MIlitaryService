from fastapi import APIRouter
from .items.views import router as itemsRouter
from .orders.views import router as ordersRouter


router = APIRouter(prefix="/api")
router.include_router(router=itemsRouter)
router.include_router(router=ordersRouter)
