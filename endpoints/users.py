from fastapi import status, APIRouter
from fastapi.responses import JSONResponse
from models.schemas import User

person = {
    "napster": {"username": "napster"},
    "juanito": {"username": "juanito"},
    "zapata": {"username": "zapata"},
}

router = APIRouter()

@router.post("/user")
async def create_user(users: User):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "User created successfully",
            "data": str(users)
        }
    )

@router.get("/user/{username}")
async def get_user(username: str):
    user = person.get(username)

    if user:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": f"User {username} found successfully",
                "data": user
            }
        )

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "message": f"User {username} not found"
        }
    )
