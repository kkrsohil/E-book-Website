
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page,name='home'),
    path('service/',views.service_page,name='service'),
    path('blog/',views.blog_page,name='blog'),
    path('add_blog/',views.add_blog,name='add_blog'),
    path('price/',views.price_page,name='price'),
    path('contact/',views.contact_page,name='contact'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)