from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls

from app_airplanes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('airplanes/estimate-fuel-consumption/', views.EstimateFuelConsumptionView.as_view()),
    path('docs/', include_docs_urls(title='Airplanes'))
]
