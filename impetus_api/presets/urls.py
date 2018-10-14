from django.urls import path
from presets import views

urlpatterns = [
    path('presets/', views.preset_list),
    path('presets/<int:pk>', views.preset_detail),
]
