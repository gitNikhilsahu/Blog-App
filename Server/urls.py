from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from App import views


urlpatterns = [
    path('accounts/', views.AccountsHome, name="accountshome"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.article_home, name="articlehome"),
    path('articlelist/', views.article_list, name="articlelist"),
    path('create/', views.article_create),
    path('retrive/<int:id>', views.article_retrive, name='articleretrive'),
    path('update/<int:id>', views.article_update, name='articleupdate'),
    path('delete/<int:id>', views.article_delete, name='articledelete'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)