from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('polls.urls')),    # Ruta raíz apunta a las URLs de polls
    path('admin/', admin.site.urls),
]
