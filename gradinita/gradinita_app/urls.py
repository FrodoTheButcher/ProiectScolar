
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
	path('admin/',admin.site.urls),
    path('navbar/',views.navbar,name="navbar"),
    path('',views.home,name="home"),
    path('inscriere/',views.inscrie,name="inscrie"),
    path('update/<str:pk>/',views.update,name="update_profile"),
    path('change_password/<str:pk>/',views.changepassword,name="change_password"),
    path('delete_account/<str:pk>/',views.delete,name="delete_account"),
    path('account/<str:pk>/',views.account,name="account"),
    path('logout/',views.logoutUser,name="logout"),
    path('login/',views.loginUser,name="login"),
    path('register_kid/',views.kid_register,name="register_kid"),
    path('kid_account/',views.kid_account,name="kid_account"),
    path('catalog/',views.catalog,name="catalog"),
    path('kid_account/<str:pk>',views.kid_account,name="kid_account"),
    path('request_kid/<str:pk>',views.request_kid,name="request_kid"),
    path('absente_motivari/<str:pk>',views.absente_motivari,name="absente_motivari"),
    path('delete_abs/<str:pk>/<str:pk2>',views.delete_absenta,name="delete_absenta"),
    path('delete_mtv/<str:pk>/<str:pk2>',views.delete_motivare,name="delete_motivare"),
    path('adauga_mtv/<str:pk>',views.adauga_motivare,name="adauga_motivare"),
    path('adauga_abs/<str:pk>',views.adauga_absenta,name="adauga_absenta"),
    path('update_kid/<str:pk>',views.update_kid,name="update_kid"),
    path('about_us/',views.about_us,name="about_us"),
    path('page_kids/',views.page_kids,name="page"),



]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)