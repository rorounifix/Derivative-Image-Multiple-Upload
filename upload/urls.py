from django.urls import path

from . import views

app_name = 'upload'
urlpatterns = [
    # /
    path('', views.HomeView.as_view(), name='index'),
    path('fileupload/', views.fileupload, name='fileupload'),
    path('album/', views.AlbumView.as_view(), name='album'),
    path('album/delete/<id>', views.delete, name='delete'),

]
