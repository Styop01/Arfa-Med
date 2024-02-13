"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core.settings import apps, __app_name__
from .auth import admin_logout, admin_login
# from rest_framework_simplejwt.views import (
#                                             TokenObtainPairView,
#                                             TokenRefreshView,
#                                             TokenVerifyView)


from core.settings import BASE_DIR

urlpatterns = [

    path('admin/login/', admin_login),
    path('admin/logout/', admin_logout),
    path('admin/', admin.site.urls),

    # # Token-based Authentication --------------------------------------------
    # path('auth/', include('djoser.urls')),  # 'home/auth/users/' returns link
    # #  to all users also add user.
    #
    # # '/home/auth/token/login/' endpoint to login(authenticate) then token
    # # will be sent.
    #
    # # authorization
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
    #
    # # SimpleJWT Authentication ----------------------------------------------
    #
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    # # Ask to receive token
    #
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # # To receive new access token
    #
    # path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
]

for item in apps:

    try:
        urlpatterns.append(
            # path('home', include(page.home.urls))
            path(f'{item}/', include(f"{__app_name__}.{item}.urls")),
                 )
    except ModuleNotFoundError:
        print(f"Not found urls in module {item}")


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
