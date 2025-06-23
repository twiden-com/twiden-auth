from fastapi import HTTPException, status
from src.modules.auth.auth_exceptions import InvalidCredentialsException, UserAlreadyExistsException, UserNotActiveException
from src.modules.auth.auth_schemas import SignUpRequest
from src.modules.auth.auth_enums import FlowType, LoginType
from src.modules.profiles.profile_enums import UserStatus
from src.modules.auth.auth_service import AuthService
from src.modules.profiles.profile_controller import ProfileController
from src.modules.organizations.organization_controller import OrganizationController
from src.modules.profiles.profile_schemas import ProfileCreateRequest


class AuthController:

    def __init__(self,
                    auth_service: AuthService,
                    profile_controller: ProfileController, 
                    organization_controller: OrganizationController
                ):
        self._auth_service            = auth_service
        self._profile_controller      = profile_controller
        self._organization_controller = organization_controller


    def signup(self, request: SignUpRequest):
        try:
            org_id = request.meta_data.org_id
            user_org_email = request.email.split('@')[0] + '+' + org_id + request.email.split('@')[1]
            

            user = self._auth_service.sign_up(request.email, request.password)
            
            # profile =  self._profile_controller.create_profile(
            #             ProfileCreateRequest(
            #                 user_id    = user.id,
            #                 email      = request.email,
            #                 first_name = request.first_name,
            #                 last_name  = request.last_name,
            #                 gender     = request.gender
            #             )
            #         )
            return user
        except UserAlreadyExistsException as e:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=e.message)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")