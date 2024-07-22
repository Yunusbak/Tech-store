from django.urls import path
from .views import home_view, register_view, login_view, account_view, logout_view, phone_view, phone_detail_view, accessories_view, accessories_detail_view, laptop_view, laptop_detail_view, phone_create, accessories_create, laptop_create, phone_delete, laptop_delete, accessories_delete, phone_update, laptop_update, accessories_update, info, search_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", home_view, name="home"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("account/", account_view, name="account"),
    path("logout/", logout_view, name="logout"),
    path("info/", info, name="info"),

    path("phone/", phone_view, name="phone"),
    path("laptop/", laptop_view, name="laptop"),
    path("accessories/", accessories_view, name="accessories"),

    path("phone_detail/<int:id>/", phone_detail_view, name="phone_detail"),
    path("laptop_detail/<int:id>/", laptop_detail_view, name="laptop_detail"),
    path("accessories_detail/<int:id>/", accessories_detail_view, name="accessories_detail"),



    path("phone_create/", phone_create, name="phone-create"),
    path("laptop_create/", laptop_create, name="laptop-create"),
    path("accessories_create/", accessories_create, name="accessories-create"),


    path("phone_delete/<int:id>/", phone_delete, name="phone-delete"),
    path("laptop_delete/<int:id>/", laptop_delete, name="laptop-delete"),
    path("accessories_delete/<int:id>/", accessories_delete, name="accessories-delete"),

    path("phone_update/<int:id>/", phone_update, name="phone-update"),
    path("laptop_update/<int:id>/", laptop_update, name="laptop-update"),
    path("accessories_update/<int:id>/", accessories_update, name="accessories-update"),

    path("search/", search_view, name="search")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)