import logging
from typing import List, Optional

from apps.resincore.exceptions.exceptions import LogicalException
from apps.resincore.models.guide import Guide
from apps.resincore.models.guide_item import GuideItem


class GuideItemService:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_by_id(self, id: int) -> Optional[GuideItem]:
        guide_item = GuideItem.objects.filter(id=id).first()
        self.logger.debug(f"GET GUIDE ITEM BY ${id}. RESULT ${guide_item}")
        return guide_item

    def get_by_code(self, code: str) -> Optional[GuideItem]:
        guide_item = GuideItem.objects.filter(code=code).first()
        self.logger.debug(f"GET GUIDE ITEM BY CODE ${code}. RESULT ${guide_item}")
        return guide_item

    def get_by_guide(self, guide_id: int) -> List[GuideItem]:
        guide_items = list(GuideItem.objects.filter(guide_id=guide_id).all())
        self.logger.debug(f"GET GUIDE ITEM BY GUID: {guide_id}. RESULT ${len(guide_items)}")
        return guide_items

    def create(self, guide_item: GuideItem) -> GuideItem:
        try:
            guide_item.save()
            self.logger.info(f"CREATED GUIDE ITEM: {guide_item}")
            return guide_item
        except Exception as e:
            self.logger.exception(f"ERROR WHILE CREATING GUIDE ITEM: {str(e)}")
            raise LogicalException(f"Error while creating guide item: {str(e)}") from e
