from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [

    path("super-secret-muhammad-sufyan-admin-place/login", views.login_view, name = "login"),
    path("super-secret-muhammad-sufyan-admin-place/add_articles", views.add_articles, name = "adda"),
    path("super-secret-muhammad-sufyan-admin-place/add_lectures", views.add_lectures, name = "addl"),
    path("super-secret-muhammad-sufyan-admin-place/add_image", views.add_image, name = "addi"),
    path("super-secret-muhammad-sufyan-admin-place/edit/<int:id>/<str:type>", views.edit_post, name = "edit"),
    path("super-secret-muhammad-sufyan-admin-place/all_post", views.edit_articles, name = "all_post"),
    path("super-secret-muhammad-sufyan-admin-place/delete/<int:id>/<str:type>", views.delete_post, name = "delete"),
    path("", views.article_view, name = "main"),
    path("view/lectures", views.lecture_view, name = "lv"),
    path("view/gallery", views.gallery_view, name = "gv"),
    path("post/<int:id>/<str:type>", views.post_view, name = "apv"),
    path("search", views.search, name = "sf")


] 
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)