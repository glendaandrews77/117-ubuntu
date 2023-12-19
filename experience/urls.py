from django.urls import path
from experience import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.experience_list, name='experience_list'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

