from fastapi import FastAPI, Path, Query
from typing import Optional,List
from typing import Union
from pydantic import BaseModel

from api import users, sections, courses

app = FastAPI()

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)