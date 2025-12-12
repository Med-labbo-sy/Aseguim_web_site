from django.contrib import admin
from django.urls import path, include
from django.conf import settings               # ← ajout
from django.conf.urls.static import static     # ← ajout


admin.site.site_header = "Aseguim Meknès"
admin.site.site_title = "Aseguim Admin"
admin.site.index_title = "Gestion de la plateforme"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Babalee.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # path('', include('ton_app.urls')),  # si tu as une app
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
