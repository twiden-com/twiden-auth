from fastapi import APIRouter, Depends, status
from src.config.dependencies import get_auth_controller, AuthController
from src.modules.users.user_models import SignUpRequest

router = APIRouter(prefix="/v1/auth", tags=["Authentication"])

@router.post(
    "/signup",
    response_model=dict,
    status_code=status.HTTP_201_CREATED,
    summary="Sign up a new user",
    description="Create a new user account with email and password authentication"
)
async def signup(
    signup_request  : SignUpRequest,
    auth_controller : AuthController = Depends(get_auth_controller)
):  
    
    return await auth_controller.process_signup(signup_request)