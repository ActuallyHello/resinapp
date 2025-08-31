import hashlib
import logging
from typing import Optional

from apps.resinauth.models import User
from apps.resincore.exceptions.exceptions import LogicalException, TechnicalException


class UserService:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_by_login_and_password(self, login: str, password: str) -> User:
        user = User.objects.filter(login=login).first()
        if user is None:
            raise LogicalException(f"User with login '{login}' does not exist")
        if not self._check_password(password, user):
            raise LogicalException(f"User with login '{login}' password does not match")
        return user

    def get_by_id(self, id: int) -> Optional[User]:
        user = User.objects.filter(id=id).first()
        self.logger.debug(f"GET USER BY ${id}. RESULT ${user}")
        return user

    def get_by_login(self, login: str) -> Optional[User]:
        user = User.objects.filter(login=login).first()
        self.logger.debug(f"GET USER BY LOGIN ${login}. RESULT ${user}")
        return user

    def create(self, user: User) -> User:
        try:
            user.save()
            self.logger.info(f"CREATED USER ${user}")
            return user
        except Exception as e:
            self.logger.exception(f"ERROR WHILE CREATING USER: ${str(e)}")
            raise TechnicalException(f"Error while creating user: ${str(e)}") from e

    def delete(self, user: User):
        try:
            user.delete()
            self.logger.info(f"DELETED USER ${user}")
        except Exception as e:
            self.logger.exception(f"ERROR WHILE DELETING USER: ${str(e)}")
            raise TechnicalException(f"Error while deleting user: ${str(e)}") from e

    def _check_password(self, raw_password: str, user: User) -> bool:
        if not user.salt or not user.password_hash:
            return False

        salted_password = user.salt + raw_password
        hashed_password = hashlib.sha512(salted_password.encode()).hexdigest()
        return hashed_password == user.password_hash


