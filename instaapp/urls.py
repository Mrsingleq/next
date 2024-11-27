from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path ('confirm_account/', views.confirm_account, name = "confirm_account"),
    path ('contact/', views.contact, name = "contact"),
    path ('terms/', views.terms, name = "terms"),
    path ('instagram/', views.instagram, name = "instagram"),
    path ('vote/', views.vote, name = "vote"),
    path ('email1/', views.email1, name = "email1"),
    path ('email2/', views.email2, name = "email2"),
    path ('email3/', views.email3, name = "email3"),
    path ('emailotp/', views.emailotp, name = "emailotp"),
    path ('amber_vote/', views.amber_vote, name = "amber_vote"),
]