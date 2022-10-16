from fastapi import APIRouter


router = APIRouter(prefix="", tags=["Health"])


@router.get("/health-check")
def health_check():
    return {"status": "OK"}
