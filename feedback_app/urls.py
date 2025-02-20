# urls.py
from django.urls import path
from .views import feedback_view, feedback_success

urlpatterns = [
    path('feedback/', feedback_view, name='feedback'),
   path('feedback/success/', feedback_success, name='feedback_success')

]
