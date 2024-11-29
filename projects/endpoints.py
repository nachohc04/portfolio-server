from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from projects.project_model import Project, ProjectCreate, ProjectPublic
from database.db import get_session
from sqlalchemy.orm import selectinload

project_router = APIRouter(
        tags=["Project"]
        )

@project_router.post(
        "/projects",
        status_code=status.HTTP_201_CREATED,
        response_model=ProjectPublic
)
async def create_project(
        project_data: ProjectCreate,
        session: Session = Depends(get_session)
) -> ProjectPublic:
    project = Project(**project_data.model_dump())
    session.add(project)
    session.commit()
    session.refresh(project)
    return project

@project_router.get(
    "/projects/",
    response_model=list[ProjectPublic]
)
def get_projects(
    session: Session = Depends(get_session),
    featured: bool = False,
    offset: int = 0,
    limit: int = 3,
) -> list[ProjectPublic]:
    query = select(Project)
    
    if featured:
        query = query.where(Project.featured == True)
    
    projects = session.exec(query.offset(offset).limit(limit)).all()
    return projects

@project_router.get(
    "/projects/{projectId}",
    response_model=ProjectPublic
)
def get_project(
    projectId: int,
    session: Session = Depends(get_session)
) -> ProjectPublic:
    query = (
        select(Project)
        .where(Project.id == projectId)
        .options(selectinload(Project.collaborators))  # Ensure collaborators are eagerly loaded
    )

    project = session.exec(query).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    return project