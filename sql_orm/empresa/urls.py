from django.conf.urls import url

from empresa.views import Index, EmpleadoListView
from empresa import views

urlpatterns = [
    url(r'^$', Index.as_view(),name='home'),
    url(r'all/', EmpleadoListView.as_view(),name='empleados' ),
    url(r'pdf/', views.pdfgen, name='genPDF'),
]
