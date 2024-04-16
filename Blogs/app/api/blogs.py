from fastapi import APIRouter, Depends
from uuid import UUID
from sqlmodel.ext.asyncio.session import AsyncSession
from app.core.db import get_session
from app.service.blogs import BlogServices
from app.models.blogs import BlogCreate, BlogUpdate

blogs_router = APIRouter(prefix="/blogs", tags=["Blogs"])

blog_services = BlogServices()


@blogs_router.get("/blog/{id}")
async def get_blog_id_by_id(id: UUID, session: AsyncSession = Depends(get_session)):
    return await blog_services.get_blog_id_by_id(id=id, session=session)


@blogs_router.get("/blogs")
async def get_blogs(session: AsyncSession = Depends(get_session)):
    return await blog_services.get_blogs(session=session)


@blogs_router.post("/blog")
async def create_blog(
    blog_details: BlogCreate, session: AsyncSession = Depends(get_session)
):
    return await blog_services.create_blog(blog_details=blog_details, session=session)


@blogs_router.put("/blog/{id}")
async def update_blog_id_by_id(
    id: UUID,
    blog_update_details: BlogUpdate,
    session: AsyncSession = Depends(get_session),
):
    return await blog_services.update_blog_id_by_id(
        id, blog_update_details=blog_update_details, session=session
    )


@blogs_router.delete("/blog/{id}")
async def delete_blog_id_by_id(id: UUID, session: AsyncSession = Depends(get_session)):
    return await blog_services.delete_blog_id_by_id(id=id, session=session)
