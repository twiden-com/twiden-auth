from fastapi import APIRouter, Depends, status
from src.config.dependencies import get_auth_controller, AuthController
from src.modules.profiles.profile_models import SignUpRequest

router = APIRouter(prefix="/v1/organizations", tags=["Organizations"])

@router.post(
    "/create",
    response_model=dict,
    status_code=status.HTTP_201_CREATED,
    summary="Sign up a new organization",
    description="Create a new organization for a user by owner_id"
)
async def create_org(
    signup_request  : CreateOrgRequest,
    auth_controller : AuthController = Depends(get_auth_controller)
):  
    return await auth_controller.process_signup(signup_request)