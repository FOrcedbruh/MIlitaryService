from fastapi import APIRouter, Depends, Body, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from core.db import db
from .schemas import ItemCreateSchema, ItemReadSchema, ItemUpdateSchema
from . import utils, crud

router = APIRouter(prefix="/items", tags=["Items"])



@router.post("/add")
async def index(
    session: AsyncSession = Depends(db.generate_session),
    item_in: ItemCreateSchema = Depends(utils.GetCreateItemData),
) -> dict:
    return await crud.create_item(session=session, item_in=item_in)



@router.post("/")
async def index(
    session: AsyncSession = Depends(db.generate_session),
    limit: int = Body()
) -> list[ItemReadSchema]:
    return await crud.get_items(session=session, limit=limit)


@router.patch("/append_images/{item_id}")
async def index(
    item_id: int,
    session: AsyncSession = Depends(db.generate_session),
    images: list[UploadFile] = File()
):
    return await crud.append_images_to_item(images=images, item_id=item_id, session=session)


@router.patch("/update")
async def index(
    session: AsyncSession = Depends(db.generate_session),
    item_in: ItemUpdateSchema = Depends(utils.GetUpdateItemData),
    item_id: int = Body()
) -> dict:
    return await crud.update_item(session=session, item_in=item_in, item_id=item_id)

@router.delete("/delete")
async def index(
    session: AsyncSession = Depends(db.generate_session),
    item_id: int = Body()
):
    return await crud.delete_item(session=session, item_id=item_id)