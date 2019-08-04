from django.urls import path, include

urlpatterns = [
    path('', include('presets.urls')),
    path('', include('plan.urls')),
]
