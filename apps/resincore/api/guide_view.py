from django.http import HttpRequest, JsonResponse

from apps.resincore.api.base_api_view import BaseAPIView
from apps.resincore.models.guide import Guide
from apps.resincore.models.guide_item import GuideItem
from apps.resincore.services.guide_item_service import GuideItemService
from apps.resincore.services.guide_service import GuideService
from apps.resincore.validations import validator


class GuideDetailView(BaseAPIView):
    def __init__(self):
        super().__init__()
        self.guide_service = GuideService()
        self.guide_item_service = GuideItemService()


    def get(self, request: HttpRequest, guide_id: int):
        """POST /api/guides/{guide_id} - Создать новый справочник"""
        validator.check_valid_id(guide_id)

        print(list(Guide.objects.all()))
        print(list(GuideItem.objects.all()))

        guide = self.guide_service.get_by_id(guide_id)
        if guide is None:
            return JsonResponse(
                data={f"Guide was not found by id: {guide_id}!"},
                status=404,
            )
        data = guide.to_dict()

        if request.GET.get('expand', 'false').lower() == 'true':
            guide_items = self.guide_item_service.get_by_guide(guide_id)
            data['guide_items'] = [guide_items.to_dict() for guide_items in guide_items]

        return JsonResponse(
            data=data,
            status=200
        )


class GuideByCodeView(BaseAPIView):
    def __init__(self):
        super().__init__()
        self.guide_service = GuideService()
        self.guide_item_service = GuideItemService()

    def get(self, request: HttpRequest, code: str):
        """GET /api/guides/code/{code} - Получить справочник по коду"""
        if code is None or code == '':
            return JsonResponse(
                f"Guide code is invalid!",
                status=400,
            )

        guide = self.guide_service.get_by_code(code)
        if not guide:
            return JsonResponse(
                f"Guide was not found by code: {code}!",
                status=404,
            )

        data = guide.to_dict()
        if request.GET.get('expand', 'false').lower() == 'true':
            guide_items = self.guide_item_service.get_by_guide(guide.id)
            data['guide_items'] = guide_items

        return JsonResponse(
            data=data,
            status=200
        )