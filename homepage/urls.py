from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='main.html')),
    path('company/',
         TemplateView.as_view(template_name='company/company.html')),

    path('product/weldig', TemplateView.as_view(template_name='product/welding.html')),
    path('product/expendable_weldig', TemplateView.as_view(template_name='product/expendable_weldig.html')),
    path('product/cutting', TemplateView.as_view(template_name='product/cutting.html')),
    path('product/expendable_cutting', TemplateView.as_view(template_name='product/expendable_cutting.html')),
    path('product/blasting', TemplateView.as_view(template_name='product/blasting.html')),
]
