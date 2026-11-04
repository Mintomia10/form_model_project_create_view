from django.urls import path
from formapp.views import home_view, add_studnt


urlpatterns = [
    path('', home_view, name='home_page'),
    path('add_student', add_studnt, name='addstudent_page')
]
