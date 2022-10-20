"""lenglishonlinelearning URL Configuration
"""
from lenglishonlinelearning import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("baseapp.urls")),
    path("", include("newsletter.urls")),
    path("", include("cart.urls")),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "lenglishonlinelearning.views.error_404_view"
handler500 = "lenglishonlinelearning.views.error_500_view"
