import json
import logging
from typing import Dict, Callable

from django.http import HttpRequest, JsonResponse
from django.views import View

from apps.resincore.exceptions.exceptions import TechnicalException, LogicalException


class BaseAPIView(View):
    """Базовый класс для API views"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)


    def parse_json_body(self, request) -> Dict:
        """Парсинг JSON тела запроса"""
        try:
            return json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            raise TechnicalException("Invalid JSON format")

    def check_parsed_body(self, body: Dict):
        if body is None or len(body) == 0:
            raise LogicalException("Request payload is empty")

    def dispatch(self, request, *args, **kwargs):
        """Перехватываем все запросы и обрабатываем исключения"""
        try:
            return super().dispatch(request, *args, **kwargs)
        except LogicalException as e:
            self.logger.exception(e)
            return JsonResponse(data=str(e), status=400)
        except Exception as e:
            self.logger.exception(e)
            return JsonResponse(data = {'message' : f"Internal server error: ${e}"}, status=500)
