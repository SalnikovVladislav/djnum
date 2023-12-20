from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('images/', image_list, name='image_list'),
    path('upload/', upload_image, name='upload_image'),
    path('delete/<int:image_id>/', delete_image, name='delete_image'),
    path('yes/<int:image_id>/', yes_logic, name='yes_logic'),
    path('no/<int:image_id>/', no_logic, name='no_logic'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)