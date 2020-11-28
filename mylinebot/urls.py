import os
import sys
parent_dir = os.path.dirname(sys.path[0])
from django.urls import path
from runserver.views import callback
from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mylinebot/callback/', callback)
]