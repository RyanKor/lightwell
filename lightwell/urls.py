"""lightwell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import (handler400, handler403, handler404, handler500)
from django.views.generic import TemplateView
from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # 용접기 제품
    path('product/weldig/co2-weldig/miracle-600a', TemplateView.as_view(template_name='./product/weldig/co2-weldig/miracle-600a.html')),
    path('product/weldig/co2-weldig/miracle-500a', TemplateView.as_view(template_name='./product/weldig/co2-weldig/miracle-500a.html')),
    path('product/weldig/co2-weldig/miracle-350a', TemplateView.as_view(template_name='./product/weldig/co2-weldig/miracle-350a.html')),
    path('product/weldig/co2-weldig/ship-weldig', TemplateView.as_view(template_name='./product/weldig/co2-weldig/ship-weldig.html')),

    path('product/weldig/autocarriage/no-magnet', TemplateView.as_view(template_name='./product/weldig/autocarriage/no-magnet.html')),
    path('product/weldig/autocarriage/twin-carry-auto-unit', TemplateView.as_view(template_name='./product/weldig/autocarriage/twin-carry-auto-unit.html')),
    path('product/weldig/autocarriage/magnet', TemplateView.as_view(template_name='./product/weldig/autocarriage/magnet.html')),
    path('product/weldig/autocarriage/mini-carriage', TemplateView.as_view(template_name='./product/weldig/autocarriage/mini-carriage.html')),

    path('product/weldig/submerged-weldig/lw-sub-ac-1500a', TemplateView.as_view(template_name='./product/weldig/submerged-weldig/lw-sub-ac-1500a.html')),
    path('product/weldig/submerged-weldig/lw-sub-dc-1500a', TemplateView.as_view(template_name='./product/weldig/submerged-weldig/lw-sub-dc-1500a.html')),
    path('product/weldig/submerged-weldig/sw-41-carry-auto', TemplateView.as_view(template_name='./product/weldig/submerged-weldig/sw-41-carry-auto.html')),

    path('product/weldig/dc-tig-weldig/tig-300ep', TemplateView.as_view(template_name='./product/weldig/dc-tig-weldig/tig-300ep.html')),
    path('product/weldig/dc-tig-weldig/tig-500ep', TemplateView.as_view(template_name='./product/weldig/dc-tig-weldig/tig-500ep.html')),
    path('product/weldig/dc-tig-weldig/tiger201', TemplateView.as_view(template_name='./product/weldig/dc-tig-weldig/tiger201.html')),

    path('product/weldig/arch-weldig/apollo-180', TemplateView.as_view(template_name='./product/weldig/arch-weldig/apollo-180.html')),
    path('product/weldig/arch-weldig/apollo-200', TemplateView.as_view(template_name='./product/weldig/arch-weldig/apollo-200.html')),
    path('product/weldig/arch-weldig/s-200dp', TemplateView.as_view(template_name='./product/weldig/arch-weldig/s-200dp.html')),

    # 용접기 소모품
    path('product/expendable_weldig', TemplateView.as_view(template_name='product/expendable_weldig.html')),
    # 절단기 제품
    path('product/cutting', TemplateView.as_view(template_name='product/cutting.html')),
    # 절단기 소모품
    path('product/expendable_cutting', TemplateView.as_view(template_name='product/expendable_cutting.html')),
    # Blastinc Machine
    path('product/blasting', TemplateView.as_view(template_name='product/blasting.html')),
]
