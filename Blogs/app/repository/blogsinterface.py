from abc import ABC, abstractmethod
from uuid import UUID
from sqlalchemy.ext.asyncio.session import AsyncSession
from app.models.blogs import BlogCreate, BlogUpdate


class BlogInterface(ABC):
    @abstractmethod
    def get_blog_id_by_id(self, id: UUID, session: AsyncSession):
        pass

    @abstractmethod
    def get_blogs(self, session: AsyncSession):
        pass

    @abstractmethod
    def create_blog(self, session: AsyncSession, blog_detials: BlogCreate):
        pass

    @abstractmethod
    def update_blog_id_by_id(
        self, id: UUID, session: AsyncSession, blog_update_details: BlogUpdate
    ):
        pass

    @abstractmethod
    def delete_blog_id_by_id(id: UUID, session: AsyncSession):
        pass
