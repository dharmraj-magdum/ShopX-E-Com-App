from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("shop.urls")),
    path('users/', include("users.urls")),
]

# //pick images from  local in case od development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# to import static in deployment
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
