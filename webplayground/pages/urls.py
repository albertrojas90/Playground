from django.urls import path
from . import views
from .views import PageListView, PageDetailView

# en forma de lista basada en funciones
#urlpatterns = [
#    path('', views.pages, name='pages'),
#    path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
#]

# en forma de vista basada en clases
urlpatterns = [
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
]