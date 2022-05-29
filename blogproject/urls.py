from django.contrib import admin
from django.urls import path
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('detail/<int:blog_id>', views.detail, name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #media 파일에 접근할 수 있는 url도 추가해야 함
