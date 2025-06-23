
class UserDomainException(Exception):
    pass


class UserAlreadyExistsException(UserDomainException):
    def __init__(self, email: str, org_id: str):
        super().__init__(f"User with email {email} already exists in org: {org_id}") 


class UserNotFoundException(UserDomainException):
    def __init__(self, identifier: str):
        super().__init__(f"User not found: {identifier}")


class AuthenticationException(UserDomainException):
    pass

class InvalidCredentialsException(AuthenticationException):
    """Exception for invalid login credentials"""
    def __init__(self):
        super().__init__("Invalid email or password")


class UserNotActiveException(AuthenticationException):
    """Exception when user is not active"""
    def __init__(self, user_id: str):
        super().__init__(f"User {user_id} is not active")