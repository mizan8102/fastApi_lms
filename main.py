from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Gwen",
        "email": "gwen@example.com",
    },
    license_info={
        "name": "MIT",
    },)

"""
get swag documentation use endpoint(/doc)
another type of documentation use endpoint(/redoc)
here package manager use poetry
for server install uvicorn 
start cmd   'uvicorn main:app'
reload cmd  'uvicorn main:app --reload'
"""
users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "success"


@app.get("/users/{id}")
async def get_user(
        id: int = Path(..., description="The ID of the user you want to retrieve.", gt=2),
        q: str = Query(None, max_length=5),
):
    return {"id": id, "is_active": q}
