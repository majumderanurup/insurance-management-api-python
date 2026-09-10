from fastapi import APIRouter

router = APIRouter(
    tags=["Customer"]
)


@router.get("/customers")
def get_customers():
    return [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john@example.com",
        }
    ]