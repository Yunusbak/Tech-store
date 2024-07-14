from django.urls import path
from .views import home_view, register_view, login_view, phone, laptop, accessories, account_view, logout_view, pokupka_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", home_view, name="home"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("phone/", phone, name="phone"),
    path("laptop/", laptop, name="laptop"),
    path("accessories/", accessories, name="accessories"),
    path("account/", account_view, name="account"),
    path("logout/", logout_view, name="logout"),
    path("pokupka/", pokupka_view, name="pokupka")


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)