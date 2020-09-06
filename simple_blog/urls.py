from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.conf import settings


from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('polls.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
    path('', include(('posts.urls', 'posts'), namespace='posts')),
   # path('', include(('comments.urls', 'comments'), namespace='comments')),


    path(
        route='sobre-mi',
        view=TemplateView.as_view(template_name='about.html'),
        name='about'
    ),
    path('', include(('users.urls', 'users'), namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
