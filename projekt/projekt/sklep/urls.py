from django.urls import path
from . import views

urlpatterns = [
    path('projekt/klienci', views.klienci_list),
    path('projekt/klienci/<int:pk>/',views.klient_detail),

    path('mysite_kantor/zamowienia', views.zamowienia_list),
    path('mysite_kantor/zamowienia/<int:pk>/', views.zamowienia_detail),

    path('mysite_kantor/produkty', views.produkty_list),
    path('mysite_kantor/kurs_z/<int:pk>/', views.produkty_detail),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),


]





