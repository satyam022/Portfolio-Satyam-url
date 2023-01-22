from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from Profile import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('base',views.Base,name='base'),
    path('Portfolio',views.Port_folio,name='portfolio'),
    path('Blog',views.Blog,name='blog_page'),
    path('contact',views.Contact,name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
