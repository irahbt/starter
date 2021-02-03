from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('checkout_subscription/', include('checkout_subscription.urls')),
    path('profile/', include('profiles.urls')),
    path('subscribe/', include('subscribe.urls')),
    path('recipes/', include('recipes.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
