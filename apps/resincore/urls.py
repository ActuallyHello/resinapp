from django.urls import path

from apps.resincore.api.guide_view import GuideDetailView

urlpatterns = [
    path('guides/<int:guide_id>/', GuideDetailView.as_view(), name='guide-detail-by-id'),
    path('guides/<str:guide_code>/', GuideDetailView.as_view(), name='guide-detail-by-code'),
]
