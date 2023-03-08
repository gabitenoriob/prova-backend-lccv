from django.urls import path
from .views import IndexView
from .views import PaginaInicial 


urlpatterns = [
    path('inicio/', IndexView.as_view(), name='inicio' ),
    path('', PaginaInicial.as_view(), name='index' ),
    
]
