from src.modules.organizations.organization_schemas import UserMembershipRequest


class OrganizationController:

    def __init__(self, organization_service):
        self._organization_service = organization_service


    # def get_user_memberhip(self, request: UserMembershipRequest):
    #     pass

