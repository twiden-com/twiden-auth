from src.modules.auth.auth_schemas import SignUpRequest
from src.modules.auth.auth_enums import FlowType
from src.modules.users.user_schemas import DBProfileCreate
from src.modules.users.user_enums import UserStatus

class AuthController:

    def __init__(self, user_controller):
        self._user_controller = user_controller

    def signup(self, signup_request: SignUpRequest):
        user_id = ""

        DBProfileCreate(
            first_name = signup_request.first_name,
            last_name  = signup_request.last_name,
            gender     = signup_request.gender,
            email      = signup_request.email,
            status     = UserStatus.ACTIVE.value
        )

    def signup_c2b():
        pass