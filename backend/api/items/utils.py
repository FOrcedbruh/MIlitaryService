from fastapi import Body
from .schemas import ItemCreateSchema


def GetCreateItemData(
    item_in: ItemCreateSchema = Body()
) -> ItemCreateSchema:
    return ItemCreateSchema(
        item_name=item_in.item_name,
        description=item_in.description,
        limit=item_in.limit,
        cost=item_in.cost,
        images=item_in.images
    )