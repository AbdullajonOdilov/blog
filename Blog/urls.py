
from django.contrib import admin
from django.urls import path

from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('register/',RegisterView.as_view()),
    path('maqola/',BlogView.as_view()),
    path('maqola/<int:pk>/',TanlanganView.as_view()),
]
