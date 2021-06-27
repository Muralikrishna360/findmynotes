from django.urls import path

from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    path('download', views.download, name='download'),
    path('upload', views.upload, name='upload'),
    path('create_book', views.create_book, name='create_book'),
    path('report', views.report, name='report'),
    path('about', views.about, name='about'),

]