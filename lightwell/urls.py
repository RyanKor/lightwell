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
from django.conf.urls import (
    handler400, handler403, handler404, handler500)  # Error Handling
from django.views.generic import TemplateView
from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 메인화면
    path('', TemplateView.as_view(template_name='./main.html')),
    # 회사소개
    path('company', TemplateView.as_view(
        template_name='./company/company_info.html')),  # 회사 소개
    path('company/history',
         TemplateView.as_view(template_name='./company/company_history.html')),
    path('company/field',
         TemplateView.as_view(template_name='./company/company_field.html')),
    path('company/certificate', TemplateView.as_view(
        template_name='./company/company_cert.html')),  # 회사 소개
    path('company/access',
         TemplateView.as_view(template_name='./company/company_access.html')),

    # 이산화탄소 용접기 제품
    path('product/weldig/co2-weldig/miracle-600a', TemplateView.as_view(
        template_name='./product/weldig/co2-weldig/miracle-600a.html')),
    path('product/weldig/co2-weldig/miracle-500a', TemplateView.as_view(
        template_name='./product/weldig/co2-weldig/miracle-500a.html')),
    path('product/weldig/co2-weldig/miracle-350a', TemplateView.as_view(
        template_name='./product/weldig/co2-weldig/miracle-350a.html')),
    path('product/weldig/co2-weldig/ship-weldig',
         TemplateView.as_view(template_name='./product/weldig/co2-weldig/ship-weldig.html')),

    # 오토캐리지 용접기 제품
    path('product/weldig/autocarriage/no-magnet',
         TemplateView.as_view(template_name='./product/weldig/autocarriage/no-magnet.html')),
    path('product/weldig/autocarriage/twin-carry-auto-unit', TemplateView.as_view(
        template_name='./product/weldig/autocarriage/twin-carry-auto-unit.html')),
    path('product/weldig/autocarriage/magnet',
         TemplateView.as_view(template_name='./product/weldig/autocarriage/magnet.html')),
    path('product/weldig/autocarriage/mini-carriage', TemplateView.as_view(
        template_name='./product/weldig/autocarriage/mini-carriage.html')),

    # 서브 머지드 용접기 경로 매핑
    path('product/weldig/submerged-weldig/lw-sub-ac-1500a', TemplateView.as_view(
        template_name='./product/weldig/submerged-weldig/lw-sub-ac-1500a.html')),
    path('product/weldig/submerged-weldig/lw-sub-dc-1500a', TemplateView.as_view(
        template_name='./product/weldig/submerged-weldig/lw-sub-dc-1500a.html')),
    path('product/weldig/submerged-weldig/sw-41-carry-auto', TemplateView.as_view(
        template_name='./product/weldig/submerged-weldig/sw-41-carry-auto.html')),

    # 티거 용접기 경로 매핑
    path('product/weldig/dc-tig-weldig/tig-300ep', TemplateView.as_view(
        template_name='./product/weldig/dc-tig-weldig/tig-300ep.html')),
    path('product/weldig/dc-tig-weldig/tig-500ep', TemplateView.as_view(
        template_name='./product/weldig/dc-tig-weldig/tig-500ep.html')),
    path('product/weldig/dc-tig-weldig/tiger201',
         TemplateView.as_view(template_name='./product/weldig/dc-tig-weldig/tiger201.html')),

    # 아크 용접기 경로 매핑
    path('product/weldig/arch-weldig/apollo-180',
         TemplateView.as_view(template_name='./product/weldig/arch-weldig/apollo-180.html')),
    path('product/weldig/arch-weldig/apollo-200',
         TemplateView.as_view(template_name='./product/weldig/arch-weldig/apollo-200.html')),
    path('product/weldig/arch-weldig/s-200dp',
         TemplateView.as_view(template_name='./product/weldig/arch-weldig/s-200dp.html')),

    # gouging_welding.html
    path('product/weldig/gouging',
         TemplateView.as_view(template_name='./product/weldig/gouging/gouging_welding.html')),

    # 선상판넬 매핑 shipboard_panel.html
    path('product/weldig/shipboard_panel',
         TemplateView.as_view(template_name='./product/weldig/shipboard/shipboard_panel.html')),

    # 용접기 소모품 - CO2
    path('product/welding-expendable/expendable_co2',
         TemplateView.as_view(template_name='product/welding-expendable/expendable_co2.html')),
    # 용접기 소모품 - Auto Carriage
    path('product/welding-expendable/expendable_auto',
         TemplateView.as_view(template_name='product/welding-expendable/expendable_auto_carriage.html')),
    # 용접기 소모품 - TIG
    path('product/welding-expendable/expendable_tig',
         TemplateView.as_view(template_name='product/welding-expendable/expendable_tig.html')),
    # 용접기 소모품 - Regulator
    path('product/welding-expendable/expendable_regulator',
         TemplateView.as_view(template_name='product/welding-expendable/expendable_regulator.html')),
    # 절단기 제품
    path('product/cutting', TemplateView.as_view(template_name='product/cutting.html')),
    # 절단기 소모품
    path('product/expendable_cutting',
         TemplateView.as_view(template_name='product/cutter-expendable/cutter-expendable.html')),
    # Blastinc Machine
    # path('product/blasting',
    #      TemplateView.as_view(template_name='product/blasting.html')),

    # 절단기 제품
    path('product/cutter/2d_plasma',
         TemplateView.as_view(template_name='product/cutter/2d_plasma.html')),
    path('product/cutter/3d_link_plasma',
         TemplateView.as_view(template_name='product/cutter/3d_link_plasma.html')),
    path('product/cutter/bending_machine',
         TemplateView.as_view(template_name='product/cutter/bending_machine.html')),
    path('product/cutter/cnc_gas',
         TemplateView.as_view(template_name='product/cutter/cnc_gas.html')),
    path('product/cutter/cold_rolling',
         TemplateView.as_view(template_name='product/cutter/cold_rolling.html')),
    path('product/cutter/cutting_machine',
         TemplateView.as_view(template_name='product/cutter/cutting_machine.html')),
    path('product/cutter/elbow_cutting_machine',
         TemplateView.as_view(template_name='product/cutter/elbow_cutting_machine.html')),
    path('product/cutter/flame_planer',
         TemplateView.as_view(template_name='product/cutter/flame_planer.html')),
    path('product/cutter/high_frequency_bending_machine',
         TemplateView.as_view(template_name='product/cutter/high_frequency_bending_mahcine.html')),
    path('product/cutter/pipe_coaster',
         TemplateView.as_view(template_name='product/cutter/pipe_coaster.html')),
    path('product/cutter/pipe_gas_cutting_machine',
         TemplateView.as_view(template_name='product/cutter/pipe_gas_cutting_machine.html')),
    path('product/cutter/pipe_rotator',
         TemplateView.as_view(template_name='product/cutter/pipe_rotator.html')),
    path('product/cutter/positioner',
         TemplateView.as_view(template_name='product/cutter/positioner.html')),

    # 카탈로그
    path('catalogue',
         TemplateView.as_view(template_name='catalogue/catalogue.html')),

    # 연락처
    path('contact',
         TemplateView.as_view(template_name='contact/contact.html')),


############################# 이 아래부터 영문 페이지 url mapping #############################
    # 메인화면
    path('en', TemplateView.as_view(template_name='./en/main.html')),

    # 회사 소개
    path('en/company', 
         TemplateView.as_view(template_name='./en/company/company_info.html')),  # 회사 소개
    path('en/company/history',
         TemplateView.as_view(template_name='./en/company/company_history.html')),
    path('en/company/field',
         TemplateView.as_view(template_name='./en/company/company_field.html')),
    path('en/company/certificate', TemplateView.as_view(
        template_name='./en/company/company_cert.html')),  # 회사 소개
    path('en/company/access',
         TemplateView.as_view(template_name='./en/company/company_access.html')),


    # 이산화탄소 용접기 제품
    path('en/product/weldig/co2-weldig/miracle-600a', TemplateView.as_view(
        template_name='./en/product/weldig/co2-weldig/miracle-600a.html')),
    path('en/product/weldig/co2-weldig/miracle-500a', TemplateView.as_view(
        template_name='./en/product/weldig/co2-weldig/miracle-500a.html')),
    path('en/product/weldig/co2-weldig/miracle-350a', TemplateView.as_view(
        template_name='./en/product/weldig/co2-weldig/miracle-350a.html')),
    path('en/product/weldig/co2-weldig/ship-weldig',
         TemplateView.as_view(template_name='./en/product/weldig/co2-weldig/ship-weldig.html')),

    # 오토캐리지 용접기 제품
    path('en/product/weldig/autocarriage/no-magnet',
         TemplateView.as_view(template_name='./en/product/weldig/autocarriage/no-magnet.html')),
    path('en/product/weldig/autocarriage/twin-carry-auto-unit', TemplateView.as_view(
        template_name='./en/product/weldig/autocarriage/twin-carry-auto-unit.html')),
    path('en/product/weldig/autocarriage/magnet',
         TemplateView.as_view(template_name='./en/product/weldig/autocarriage/magnet.html')),
    path('en/product/weldig/autocarriage/mini-carriage', TemplateView.as_view(
        template_name='./en/product/weldig/autocarriage/mini-carriage.html')),

    # 서브 머지드 용접기 경로 매핑
    path('en/product/weldig/submerged-weldig/lw-sub-ac-1500a', TemplateView.as_view(
        template_name='./en/product/weldig/submerged-weldig/lw-sub-ac-1500a.html')),
    path('en/product/weldig/submerged-weldig/lw-sub-dc-1500a', TemplateView.as_view(
        template_name='./en/product/weldig/submerged-weldig/lw-sub-dc-1500a.html')),
    path('en/product/weldig/submerged-weldig/sw-41-carry-auto', TemplateView.as_view(
        template_name='./en/product/weldig/submerged-weldig/sw-41-carry-auto.html')),

    # 티거 용접기 경로 매핑
    path('en/product/weldig/dc-tig-weldig/tig-300ep', TemplateView.as_view(
        template_name='./en/product/weldig/dc-tig-weldig/tig-300ep.html')),
    path('en/product/weldig/dc-tig-weldig/tig-500ep', TemplateView.as_view(
        template_name='./en/product/weldig/dc-tig-weldig/tig-500ep.html')),
    path('en/product/weldig/dc-tig-weldig/tiger201',
         TemplateView.as_view(template_name='./en/product/weldig/dc-tig-weldig/tiger201.html')),

    # 아크 용접기 경로 매핑
    path('en/product/weldig/arch-weldig/apollo-180',
         TemplateView.as_view(template_name='./en/product/weldig/arch-weldig/apollo-180.html')),
    path('en/product/weldig/arch-weldig/apollo-200',
         TemplateView.as_view(template_name='./en/product/weldig/arch-weldig/apollo-200.html')),
    path('en/product/weldig/arch-weldig/s-200dp',
         TemplateView.as_view(template_name='./en/product/weldig/arch-weldig/s-200dp.html')),
    # 선상판넬 매핑 shipboard_panel.html
    path('en/product/weldig/shipboard_panel',
         TemplateView.as_view(template_name='./en/product/weldig/shipboard/shipboard_panel.html')),
    # gouging_welding.html
    path('en/product/weldig/gouging',
         TemplateView.as_view(template_name='./en/product/weldig/gouging/gouging_welding.html')),

    ########## 용접기 제품 끝 ###########


    ########## 절단기 소모품 경로 ###########
    # 절단기 소모품
    path('en/product/expendable_cutting',
         TemplateView.as_view(template_name='./en/product/cutter-expendable/cutter-expendable.html')),
    ########## 절단기 소모품 끝 ###########

    # 카탈로그
    path('en/catalogue',
         TemplateView.as_view(template_name='./en/catalogue/catalogue.html')),

    # 연락처
    path('en/contact',
         TemplateView.as_view(template_name='./en/contact/contact.html')),
]
