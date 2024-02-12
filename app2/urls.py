from . import views
from django.urls import path

urlpatterns = [
    path('second/', views.secondpage,name="secondpage")
]