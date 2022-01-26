"""web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from closest_points.views import sequential_search
from closest_points.views import comprehension_search
from closest_points.views import generator_search
from closest_points.views import mprocessing_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sequential/', sequential_search),
    path('comprehension/', comprehension_search),
    path('generators/', generator_search),
    path('multiprocessing/', mprocessing_search)
]
