from app.database.models import async_session  # створення асинхронних сесій для взаємодії з БД
from app.database.models import User, Category, Item
from sqlalchemy import select


async def set_user(tg_id: int) -> None:
    async with async_session() as session:  # зберігаємо асинхронну сесію у змінну sesion
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        # scalar(): This method returns the first column of the first row in the result.
        # If the result is empty, it returns None
        # user = await session.execute(select(User.id).where(User.tg_id == tg_id))
        # те ж саме, тільки без scalar()

        if not user:
            session.add(User(tg_id=tg_id))  # створюється новий об'єкт User і додається в сесію
            await session.commit()  # зберігаємо зміни в БД


async def get_categories():
    async with async_session() as session:  # створення асинхронних сесій для взаємодії з БД
        return await session.scalars(select(Category))  # отримуємо об'єкти з БД повністю, не тільки id


async def get_category(category_id):  # отримуємо ім'я категорії по PK
    async with async_session() as session:  # створення асинхронних сесій для взаємодії з БД
        result = await session.scalars(select(Category.name).where(Category.id == category_id))
        return result.one()


async def get_item(item_id):  # отримуємо Item по PK
    async with async_session() as session:  # створення асинхронних сесій для взаємодії з БД
        result = await session.scalars(select(Item).where(Item.id == item_id))
        return result.one()


async def get_category_item(category_id):
    async with async_session() as session:  # створення асинхронних сесій для взаємодії з БД
        # отримуємо всі Item, що відповідають даній категорії
        return await session.scalars(select(Item).where(Item.category == category_id))
