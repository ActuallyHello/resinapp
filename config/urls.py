# from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),

    # API v1 с префиксом
    path('api/v1/', include([
        # Auth приложение
        # path('auth/', include('apps.resinauth.urls')),

        # Core приложение
        path('core/', include('apps.resincore.urls')),

    ])),

    # Health check и другие общие endpoints
    path('health/', lambda request: JsonResponse({'status': 'ok'})),
]