from sqlmodel import Field, SQLModel
from typing import Optional

class ProjectBase(SQLModel):
    name: str = Field(index=True)
    host_url: str = Field(index=True)
    description: str = Field(index=True)
    image: str = Field(index=True)
    repository: str = Field(index=True)
    featured: bool = Field(defaul=False, index=True)
    collaborators: Optional[str] = None

class Project(ProjectBase, table=True):  # Mapped to the database table
    id: Optional[int] = Field(default=None, primary_key=True)

class ProjectCreate(ProjectBase):  # For creating projects (input)
    pass

class ProjectPublic(ProjectBase):  # For returning project data (output)
    id: int

class ProjectUpdate(SQLModel):  # To allow updates
    name: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    repository: Optional[str] = None
    collaborators: Optional[str] = None
    collaborators: Optional[bool] = None

