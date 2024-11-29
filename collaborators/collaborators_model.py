from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

class CollaboratorBase(SQLModel):
    name: str = Field(index=True)
    description: str = Field(index=True)
    image: str = Field(index=True)
    repository: str = Field(index=True)

class Collaborator(CollaboratorBase, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True)
    project_id: Optional[int] = Field(foreign_key="project.id")  # Foreign key to Project
    project: Optional["Project"] = Relationship(back_populates="collaborators")


class CollaboratorCreate(CollaboratorBase):  
    project_id: int

class CollaboratorPublic(CollaboratorBase):  
    id: int
    project_id: int