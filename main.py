# dynamic
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from database.db import create_db_and_tables
from contextlib import asynccontextmanager
# static
from fastapi.staticfiles import StaticFiles
from starlette.middleware.trustedhost import TrustedHostMiddleware
# routers
from projects.endpoints import project_router
from collaborators.endpoints import collaborator_router
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

origins = [
    "https://portfolio-client-orpin.vercel.app"
        ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]
)
app.add_middleware(HTTPSRedirectMiddleware)

app.include_router(project_router)
app.include_router(collaborator_router)

app.mount("/static", StaticFiles(directory="static"), name="static")
