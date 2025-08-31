import logging
from typing import Optional

from apps.resincore.exceptions.exceptions import LogicalException
from apps.resincore.models.guide import Guide


class GuideService:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_by_id(self, id: int) -> Optional[Guide]:
        guide = Guide.objects.filter(id=id).first()
        self.logger.debug(f"GET GUIDE BY ${id}. RESULT ${guide}")
        return guide

    def get_by_code(self, code: str) -> Optional[Guide]:
        guide = Guide.objects.filter(code=code).first()
        self.logger.debug(f"GET USER BY CODE ${code}. RESULT ${guide}")
        return guide

    def create(self, guide: Guide) -> Guide:
        try:
            guide.save()
            self.logger.info(f"CREATED GUIDE: {guide}")
            return guide
        except Exception as e:
            self.logger.exception(f"ERROR WHILE CREATING GUIDE: {str(e)}")
            raise LogicalException(f"Error while creating guide: {str(e)}") from e

    @staticmethod
    def build(id: int = None, label: str = None, code: str = None):
        guide = Guide()
        guide.id = id
        guide.label = label
        guide.code = code
        return guide
