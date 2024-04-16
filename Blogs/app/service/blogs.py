from app.repository.blogs import Blog
from sqlmodel.ext.asyncio.session import AsyncSession
from app.models.blogs import BlogCreate, BlogUpdate
from uuid import UUID

class BlogServices:
    def __init__(self):
        self.repository = Blog()

    async def get_blog_id_by_id(self, id:UUID, session:AsyncSession):
        return await self.repository.get_blog_id_by_id(id=id, session=session)

    async def get_blogs(self, session:AsyncSession):
        return await self.repository.get_blogs(session=session)

    async def create_blog(self, blog_details:BlogCreate, session: AsyncSession):
        return await self.repository.create_blog(blog_details=blog_details, session=session)

    async def update_blog_id_by_id(self, id: UUID, session:AsyncSession, blog_update_details:BlogUpdate):
        return await self.repository.update_blog_id_by_id(id=id, session=session, blog_update_details=blog_update_details)

    async def delete_blog_id_by_id(self,id:UUID, session:AsyncSession):
        return await self.repository.delete_blog_id_by_id(id=id, session=session )

    