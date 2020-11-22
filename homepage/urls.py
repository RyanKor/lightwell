from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='main.html')),
    path('company/',
         TemplateView.as_view(template_name='company/company.html')),

    # 용접기 제품
    path('product/weldig', TemplateView.as_view(template_name='product/welding.html')),
    # 용접기 소모품
    path('product/expendable_weldig', TemplateView.as_view(template_name='product/expendable_weldig.html')),
    # 절단기 제품
    path('product/cutting', TemplateView.as_view(template_name='product/cutting.html')),
    # 절단기 소모품
    path('product/expendable_cutting', TemplateView.as_view(template_name='product/expendable_cutting.html')),
    # Blastinc Machine
    path('product/blasting', TemplateView.as_view(template_name='product/blasting.html')),
]
