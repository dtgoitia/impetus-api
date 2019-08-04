from django.urls import path
from plan import views


urlpatterns = [
    path('api/plans', views.plans),
    # path('api/plans/<int:pk>', views.plan),
]
