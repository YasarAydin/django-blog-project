from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('blogs/', views.blogs, name="blogs"),
    path('blog-detail/<slug:slug>/', views.blog_detail, name="blog_detail"),
    path("category/<slug:slug>/", views.blog_by_category, name="blog_by_category")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
