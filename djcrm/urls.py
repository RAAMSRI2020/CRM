from django.contrib import admin
from django.urls import path
from leads.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page)
]
