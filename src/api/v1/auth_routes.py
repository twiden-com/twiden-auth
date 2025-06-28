from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from src.config.dependencies import get_auth_controller, AuthController
from src.modules.auth.auth_schemas import SignUpRequest, SignUpResponse, SignInRequest, SignInResponse, GetSignedInUserResponse, GetSignedInUserRequest

router = APIRouter(prefix="/v1/auth", tags=["Authentication"])

@router.post(
    "/signup",
    response_model=SignUpResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Sign up a new user",
    description="Create a new user account with email and password authentication"
)
async def signup(
    request         : SignUpRequest,
    auth_controller : AuthController = Depends(get_auth_controller)
):  
    return await auth_controller.signup(request)


@router.post(
    "/signin",
    response_model=SignInResponse,
    status_code=status.HTTP_200_OK,
    summary="Sign In an existing user",
    description="Signin an existing user account with email and password authentication"
)
async def signin(
    request         : SignInRequest,
    auth_controller : AuthController = Depends(get_auth_controller)
):  
    return await auth_controller.signin(request)


@router.post(
    "/me",
    response_model=GetSignedInUserResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Current Signed In user",
    description="Signin an existing user account with email and password authentication"
)
async def get_signed_in_user(
    request         : GetSignedInUserRequest,
    auth_controller : AuthController = Depends(get_auth_controller)
):  
    return await auth_controller.get_signed_in_user(request)



