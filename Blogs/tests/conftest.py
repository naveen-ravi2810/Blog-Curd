from collections.abc import Generator
from fastapi.testclient import TestClient
import pytest

from main import app
from app.core.db import get_session


from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.config import settings


async_engine: AsyncEngine = create_async_engine(settings.test_db_uri)

async_session = async_sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)

async def override_get_session():
    async with async_session() as session:
        yield session

app.dependency_overrides[get_session] = override_get_session

@pytest.fixture(scope="session")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app=app) as c:
        yield c

