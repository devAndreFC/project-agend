from django.urls import path
from contact import views

app_name = 'contact'
urlpatterns = [
    path('search/', views.search, name='search'),    
    path('<int:contact_id>/detail/', views.contact, name='contact'),
    path('<int:contact_id>/update/', views.update, name='update'),
    path('<int:contact_id>/delete/', views.delete, name='delete'),
    path('contact/create/', views.create, name='create'),

    path('', views.index, name='index'),

    # user
    path('user/create', views.register, name='register'),
]
