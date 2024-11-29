from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from collaborators.collaborators_model import CollaboratorPublic, CollaboratorCreate, Collaborator
from database.db import get_session

collaborator_router = APIRouter(
        tags=["Collaborator"]
        )

@collaborator_router.post(
        "/Collaborators",
        status_code=status.HTTP_201_CREATED,
        response_model=CollaboratorPublic
)
async def create_collaborator(
        collaborator_data: CollaboratorCreate,
        session: Session = Depends(get_session)
) -> CollaboratorPublic:
    collaborator = Collaborator(**collaborator_data.model_dump())
    session.add(collaborator)
    session.commit()
    session.refresh(collaborator)

    return collaborator
