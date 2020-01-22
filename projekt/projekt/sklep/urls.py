from django.urls import path
from . import views

urlpatterns = [
    path('projekt/klienci', views.klienci_list),
    path('projekt/klienci/<int:pk>/',views.klient_detail),

    path('projekt/zamowienia', views.zamowienia_list),
    path('projekt/zamowienia/<int:pk>/', views.zamowienia_detail),

    path('projekt/produkty', views.produkty_list),
    path('projekt/produkty/<int:pk>/', views.produkty_detail),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),


]





