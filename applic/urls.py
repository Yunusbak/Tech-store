from django.urls import path
from .views import (home,  info, search, account,  RegisterView, LoginView, LogoutView,PhoneListView, PhoneDetailView, PhoneCreateView, PhoneUpdateView, PhoneDeleteView,LaptopListView, LaptopDetailView, LaptopCreateView, LaptopUpdateView, LaptopDeleteView,AccessoriesListView, AccessoriesDetailView, AccessoriesCreateView, AccessoriesUpdateView, AccessoriesDeleteView)

urlpatterns = [
    path("", home, name = "home"),
    path("info/", info, name = "info"), 
    path("search/", search, name = "search"),
    path("account/", account, name = 'account'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Phone 
    path('phones/', PhoneListView.as_view(), name='phone'),
    path('phones/<int:pk>/', PhoneDetailView.as_view(), name='phone_detail'),
    path('phones/create/', PhoneCreateView.as_view(), name='phone-create'),
    path('phones/<int:pk>/update/', PhoneUpdateView.as_view(), name='phone-update'),
    path('phones/<int:pk>/delete/', PhoneDeleteView.as_view(), name='phone-delete'),

    # Laptop 
    path('laptops/', LaptopListView.as_view(), name='laptop'),
    path('laptops/<int:pk>/', LaptopDetailView.as_view(), name='laptop_detail'),
    path('laptops/create/', LaptopCreateView.as_view(), name='laptop-create'),
    path('laptops/<int:pk>/update/', LaptopUpdateView.as_view(), name='laptop-update'),
    path('laptops/<int:pk>/delete/', LaptopDeleteView.as_view(), name='laptop-delete'),

    # Accessories 
    path('accessories/', AccessoriesListView.as_view(), name='accessories'),
    path('accessories/<int:pk>/', AccessoriesDetailView.as_view(), name='accessories_detail'),
    path('accessories/create/', AccessoriesCreateView.as_view(), name='accessories-create'),
    path('accessories/<int:pk>/update/', AccessoriesUpdateView.as_view(), name='accessories-update'),
    path('accessories/<int:pk>/delete/', AccessoriesDeleteView.as_view(), name = 'accessories-delete')
]