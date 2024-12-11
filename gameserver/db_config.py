from sqlalchemy.ext.asyncio import create_async_engine, AsyncConnection
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///game.db"

engine = create_async_engine(DATABASE_URL, echo=True)


async def get_connection() -> AsyncConnection:
    return await engine.connect()


async def get_session() -> AsyncSession:
    session_maker = async_sessionmaker(engine)
    return session_maker()