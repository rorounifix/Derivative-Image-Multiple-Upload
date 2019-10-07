from django.urls import path

from . import views

app_name = 'upload'
urlpatterns = [
    # /
    path('', views.index, name='index'),
    path('album/', views.album, name='album'),

]
