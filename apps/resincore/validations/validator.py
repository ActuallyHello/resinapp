from apps.resincore.exceptions.exceptions import LogicalException


def check_valid_id(id: int):
    if not type(id) is int:
        raise LogicalException('ID must be integer!')
    if id <= 0:
        raise LogicalException("ID cannot be negative!")
