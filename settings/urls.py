"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from rest_framework import routers

from pay_stubs.views.employee_viewset import EmployeeViewSet
from pay_stubs.views.pay_stubs_viewset import PayStubsViewSet
from pay_stubs.views.position_viewset import PositionViewSet
from pay_stubs.views.generate_all_viewset import GenerateAllViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'funcionarios', EmployeeViewSet)
router.register(r'holerites',PayStubsViewSet)
router.register(r'cargos',PositionViewSet)
router.register(r'gerar_todos', GenerateAllViewSet, basename="Gerar holerite de todos funcionários")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]








