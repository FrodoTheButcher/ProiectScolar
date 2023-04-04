
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
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
    path('page_kids_dino/',views.page_kids,name="page1"),
    path('page_kids_momsday/',views.page_kids2,name="page2"),
        path('page_kids_violent/',views.page_kids3,name="page3"),


    path('delete_abs/<str:pk>/',views.adauga_copil_PARINTE,name="add_kid_parent"),
    path('verificare/<str:pk>/<str:newpassword>/',views.verification_gmail,name="gmail"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), name='password_reset_complete'),
    path('send_gmail/<str:pk>',views.send_gmail,name="send_gmail"),
    path('send_gmail_default',views.send_gmail_DEFAULT,name="send_gmail_DEFAULT")
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)