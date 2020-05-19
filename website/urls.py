from django.urls import path, include
from .views import hello_blog
from .views import post_detail, save_form
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', hello_blog, name='home_blog'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('save-form/', save_form, name='save_form'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
