from fastapi import APIRouter
from .items.views import router as itemsRouter



router = APIRouter(prefix="/api")
router.include_router(router=itemsRouter)
