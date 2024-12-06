from fastapi import status, HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import Item
from .schemas import ItemCreateSchema, ItemReadSchema, ItemUpdateSchema
from core.settings import settings
from core import s3_client


async def create_item(session: AsyncSession, item_in: ItemCreateSchema) -> dict:
    stmt = await session.execute(select(Item).filter(Item.item_name == item_in.item_name))
    item = stmt.scalars().first()

    if item:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Такой товар уже существует"
        )
    
    new_item = Item(**item_in.model_dump())

    session.add(new_item)
    await session.commit()

    return {
        "status": status.HTTP_201_CREATED,
        "detail": "Товар усвешно добавлен",
        "created_item": new_item
    }


async def append_images_to_item(session: AsyncSession, images: list[UploadFile], item_id: int):
    item_to_update = await session.get(Item, item_id)
    images_to_update: list[str] = []

    if not item_to_update:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail="Товар не найден"
        )
    try: 
        await s3_client.put_files(images=images)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ошибка в s3 хранилище: {e}"
        )
    for image in images:
        images_to_update.append(settings.s3cfg.get_url + "/" + image.filename)
    

    if item_to_update.images:
        item_to_update.images += images_to_update
    else:
        item_to_update.images = images_to_update

    await session.commit()

    return {
        "status": status.HTTP_200_OK,
        "detail": "Изображения успешно добавлены"
    }

    
    



async def get_items(session: AsyncSession, limit: int) -> list[ItemReadSchema]:
    stmt = await session.execute(select(Item).limit(limit=limit).offset(offset=0))
    read_items = stmt.scalars().all()

    if not read_items:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail="Товаров пока нет"
        )
    
    return list(read_items)


async def update_item(session: AsyncSession, item_in: ItemUpdateSchema, item_id: int) -> dict:
    item_for_update = await session.get(Item, item_id)


    if not item_for_update:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail="Товар не найден"
        )
    
    for name, value in item_in.model_dump(exclude_none=True).items():
        setattr(item_for_update, name, value)

    await session.commit()

    return {
        "status": status.HTTP_200_OK,
        "detail": "Товар обновлен",
    }
    


async def delete_item(session: AsyncSession, item_id: int) -> dict:
    item_for_delete = await session.get(Item, item_id)

    if not item_for_delete:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail="Товар не найден"
        )
    
    if item_for_delete.images:
        filenames: list[str] = [image[len(settings.s3cfg.get_url) + 1:] for image in item_for_delete.images]
        await s3_client.delete_objects(filenames=filenames)


    await session.delete(item_for_delete)
    await session.commit()


    return {
        "status": status.HTTP_200_OK,
        "detail": "Товар удален",
        "deleted_item": item_for_delete
    }
