from django.urls import path
from .views import FactorsView,InformationView,chart_view

urlpatterns = [

    path('factors',FactorsView.as_view()),
    path('informations',InformationView.as_view()),
    path('chart/<str:country>/', chart_view, name='chart_view'),

]
