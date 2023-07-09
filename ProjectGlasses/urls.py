"""
URL configuration for ProjectGlasses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Glasses.views import index, log_in, details, add_to_cart, cart, delete_from_cart, checkout, thank_you


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path('index/', include('django.contrib.auth.urls')),
    path('index/log_in', log_in, name="log_in"),
    path('index/details/<int:glasses_id>/', details, name='details'),
    path('add_to_cart/<int:glasses_id>/', add_to_cart, name='add_to_cart'),
    path('index/cart/', cart, name='cart'),
    path('cart/delete/<int:order_id>/', delete_from_cart, name='delete_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('thank-you/', thank_you, name='thank_you')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

