from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from .views import home_page, about_page, contact_page, login_page, register_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home_page,name='home'),
    url(r'^about/$',about_page,name='about'),
    url(r'^contact/$',contact_page,name='contact'),
    url(r'^cart/', include("carts.urls", namespace='cart')),
    url(r'^login/$',login_page,name='login'),
    url(r'^register/$',register_page,name='register'),
    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^search/', include("search.urls", namespace='search')),
    url(r'^bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
