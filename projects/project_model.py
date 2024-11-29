from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from collaborators.collaborators_model import CollaboratorPublic

class ProjectBase(SQLModel):
    name: str = Field(index=True)
    host_url: str = Field(index=True)
    description: str = Field(index=True)
    image: str = Field(index=True)
    repository: str = Field(index=True)
    featured: bool = Field(default=False, index=True)

class Project(ProjectBase, table=True):  # Mapped to the database table
    id: Optional[int] = Field(default=None, primary_key=True)
    collaborators: List["Collaborator"] = Relationship(back_populates="project")

class ProjectCreate(ProjectBase):  # For creating projects (input)
    pass

class ProjectPublic(ProjectBase):  # For returning project data (output)
    id: int
    collaborators: List[CollaboratorPublic]  # Return collaborators with the project
