import logging
from typing import Optional, List
from apps.resinauth.models import Role
from apps.resincore.exceptions.exceptions import LogicalException, TechnicalException


class RoleService:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_by_id(self, id: int) -> Optional[Role]:
        role = Role.objects.filter(id=id).first()
        self.logger.debug(f"GET ROLE BY ID: {id}. RESULT: {role}")
        return role

    def get_by_code(self, code: str) -> Optional[Role]:
        role = Role.objects.filter(code=code).first()
        self.logger.debug(f"GET ROLE BY CODE: {code}. RESULT: {role}")
        return role

    def get_all_roles(self) -> List[Role]:
        roles = list(Role.objects.all())
        self.logger.debug(f"GET ALL ROLES. COUNT: {len(roles)}")
        return roles

    def create(self, role: Role) -> Role:
        try:
            role.save()
            self.logger.info(f"CREATED ROLE: {role}")
            return role
        except Exception as e:
            self.logger.exception(f"ERROR WHILE CREATING ROLE: {str(e)}")
            raise TechnicalException(f"Error creating role: {str(e)}") from e

    def delete(self, role: Role):
        try:
            role.delete()
            self.logger.info(f"DELETED ROLE: {role}")
        except Exception as e:
            self.logger.exception(f"ERROR WHILE DELETING ROLE: {id}")
            raise TechnicalException(f"Error deleting role: {str(e)}") from e
