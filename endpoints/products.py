from fastapi import status, APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()

@router.get("/products")
async def get_products():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": ["arroz", "mantequilla"]
        }
    )
