import logging
from typing import Optional, List
from apps.resinauth.models import UserRole
from apps.resincore.exceptions.exceptions import LogicalException, TechnicalException


class UserRoleService:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_by_id(self, id: int) -> Optional[UserRole]:
        user_role = UserRole.objects.filter(id=id).first()
        self.logger.debug(f"GET USER_ROLE BY ID: {id}. RESULT: {user_role}")
        return user_role

    def get_roles_by_user(self, user_id: int) -> List[UserRole]:
        user_roles = list(UserRole.objects.filter(user_id=user_id).all())
        self.logger.debug(f"GET USER_ROLES BY USER: {user_id}. RESULT: {user_roles}")
        return user_roles

    def get_users_by_role(self, role_id: int) -> List[UserRole]:
        user_roles = list(UserRole.objects.filter(role_id=role_id).all())
        self.logger.debug(f"GET USER_ROLES BY ROLE: {role_id}. RESULT: {user_roles}")
        return list(user_roles)

    def is_user_role_exists(self, user_id: int, role_id: int) -> bool:
        exists = UserRole.objects.filter(user_id=user_id, role_id=role_id).exists()
        self.logger.debug(f"CHECK USER HAS ROLE: USER: {user_id}, ROLE: {role_id}. RESULT: {exists}")
        return exists

    def create(self, user_role: UserRole) -> UserRole:
        try:
            user_role.save()
            self.logger.info(f"CREATED USER ROLE: {user_role}")
            return user_role
        except Exception as e:
            self.logger.exception(f"ERROR WHILE CREATING USER ROLE: ${str(e)}")
            raise TechnicalException(f"Error assigning role to user: {str(e)}") from e

    def delete(self, user_role: UserRole):
        try:
            user_role.delete()
            self.logger.info(f"DELETED USER_ROLE: {user_role}")
        except Exception as e:
            self.logger.exception(f"ERROR WHILE DELETING USER ROLE: {str(e)}")
            raise TechnicalException(f"Error deleting user role: {str(e)}") from e
