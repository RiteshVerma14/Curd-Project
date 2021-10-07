from . import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('add_student/',views.add_student),
    path('update_student/',views.update_student),
]