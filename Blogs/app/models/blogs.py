from sqlmodel import SQLModel, Field
from uuid import UUID
from uuid_extensions import uuid7
from datetime import datetime

class BaseUUID(SQLModel):
    id: UUID = Field(primary_key=True, default_factory=uuid7)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(
        default_factory=datetime.now, sa_column_kwargs={"onupdate": datetime.now()}
    )

class BlogCreate(SQLModel):
    title: str
    description: str

class Blogs(BlogCreate, BaseUUID, table=True):
    status: bool = Field(default=True)

class BlogUpdate(SQLModel):
    title: str | None = None
    description: str | None = None

