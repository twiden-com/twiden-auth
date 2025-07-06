from fastapi import HTTPException, status
from src.modules.auth.auth_exceptions import InvalidCredentialsException, UserAlreadyExistsException, UserNotActiveException, OrgNotFoundException
from src.modules.auth.auth_schemas import GetSignedInUserRequest, GetSignedInUserResponse, SignUpRequest, SignUpResponse, SignInRequest, SignInResponse
from src.modules.auth.auth_enums import UserRole
from src.modules.profiles.profile_enums import UserStatus
from src.modules.auth.auth_service import AuthService
from src.modules.profiles.profile_controller import ProfileController
from src.modules.organizations.organization_controller import OrganizationController
from src.modules.profiles.profile_schemas import ProfileCreateRequest, ProfileGetRequest
from src.utils.rollback_manager import DBTransaction
from src.utils.user_utils import generate_user_org_email
import asyncio

class AuthController:

    def __init__(self,
                    auth_service: AuthService,
                    profile_controller: ProfileController, 
                    organization_controller: OrganizationController
                ):
        self._auth_service            = auth_service
        self._profile_controller      = profile_controller
        self._organization_controller = organization_controller


    async def signup(self, request: SignUpRequest):
        tx = DBTransaction()
        try:
            #1. SIGNUP USER
            email = generate_user_org_email(request.email, request.org_id)
            user  = await self._auth_service.sign_up(email, request.password)
            tx.add_rollback(self._auth_service.delete_user, user.id)

            #2. CREATE PROFILE
            profile = await self._profile_controller.create_profile(
                        ProfileCreateRequest(
                            user_id    = user.id,
                            org_id     = request.org_id,
                            email      = request.email,
                            first_name = request.first_name,
                            last_name  = request.last_name,
                            gender     = request.gender,
                            role       = UserRole.MEMBER.value
                        ),
                        as_admin=True
                    )
            tx.add_rollback(self._profile_controller.delete_user, profile.get('id'))
            
            #3. RETURN RESPONSE
            return SignUpResponse(
                message = "Signup Successfull",
                user    = user,
                profile = profile
            )
        except Exception as e:
            await tx.perform_rollbacks()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        

    async def signin(self, request: SignInRequest):
        try:
            email    = generate_user_org_email(request.email, request.org_id)
            response = await self._auth_service.sign_in(email, request.password)
            user     = response.user
            session  = response.session

            return SignInResponse(
                user_id = user.id,
                org_id  = request.org_id,
                access_token  = session.access_token,
                refresh_token = session.refresh_token,
                expires_at = session.expires_at
            )
        except Exception as e:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))
        
    
    async def get_signed_in_user(self, request: GetSignedInUserRequest):
        try:
            response = await self._auth_service.get_signed_in_user(request.access_token)
            user    = response.user
            profile = await self._profile_controller.get_profile(ProfileGetRequest( user_id=user.id))

            return GetSignedInUserResponse(
                user    = user.model_dump(),
                profile = profile
            )
        except Exception as e:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))
