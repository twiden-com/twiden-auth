from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from src.config.dependencies import get_auth_controller, AuthController
from src.modules.auth.auth_schemas import SignUpRequest

router = APIRouter(prefix="/v1/auth", tags=["Authentication"])

@router.post(
    "/signup",
    response_model=JSONResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Sign up a new user",
    description="Create a new user account with email and password authentication"
)
def signup(
    signup_request  : SignUpRequest,
    auth_controller : AuthController = Depends(get_auth_controller)
):  
    return auth_controller.signup(signup_request)

