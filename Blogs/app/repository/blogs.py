from app.repository.blogsinterface import BlogInterface
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from uuid import UUID
from app.models.blogs import Blogs, BlogCreate, BlogUpdate


class Blog(BlogInterface):
    async def get_blog_id_by_id(self, id: UUID, session: AsyncSession):
        try:
            statement = select(Blogs).where(Blogs.id == id).where(Blogs.status == True)
            blogs = (await session.exec(statement)).one_or_none()
            if blogs:
                return blogs
            raise ValueError(f"Blog at {id} is not found")
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{e}")

    async def get_blogs(self, session: AsyncSession):
        try:
            statement = select(Blogs).where(Blogs.status == True)
            blogs = (await session.exec(statement)).all()
            if blogs:
                return blogs
            raise ValueError("No blogs found")
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{e}")

    async def create_blog(self, blog_details: BlogCreate, session: AsyncSession):
        try:
            new_blog = Blogs(**jsonable_encoder(blog_details))
            session.add(new_blog)
            await session.commit()
            session.refresh(new_blog)
            return new_blog
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e}")

    async def update_blog_id_by_id(
        self, id: UUID, blog_update_details: BlogUpdate, session: AsyncSession
    ):
        try:
            statement = select(Blogs).where(Blogs.id == id).where(Blogs.status == True)
            blog = (await session.exec(statement)).one_or_none()
            if not blog:
                raise ValueError(f"No blog found in id {id}")
            blog_data = blog_update_details.model_dump(exclude_unset=True)
            blog.sqlmodel_update(blog_data)
            session.add(blog)
            await session.commit()
            session.refresh(blog)
            return blog
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{e}")

    async def delete_blog_id_by_id(self, id: UUID, session: AsyncSession):
        try:
            statement = select(Blogs).where(Blogs.id == id).where(Blogs.status == True)
            blog = (await session.exec(statement)).one_or_none()
            if not blog:
                raise ValueError(f"No blog found in id {id}")
            blog.status = False
            session.add(blog)
            await session.commit()
            return True
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{e}")
