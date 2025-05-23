from django.urls import path
from . import views
from django.urls import include

urlpatterns = [

path('generate/spec/', views.generate_spec_view, name='generate_spec'),
path('generate/coa/', views.generate_coa_view, name='generate_coa'),
path('generate/msds/', views.generate_msds_view, name='generate_msds'),
path('generate/spec-from-db/', views.select_spec_view, name='select_spec'),
path('generate/coa-from-db/', views.select_coa_view, name='select_coa'),
path('generate/msds-from-db/', views.select_msds_view, name='select_msds'),




]
