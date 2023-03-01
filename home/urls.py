from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),

    path('news-list', views.news_list, name="news_list"),
    path('news-edit/<int:newsId>', views.news_edit, name="news_edit"),
    path('news-delete/<int:newsId>', views.news_delete, name="news_delete"),
    path('create-news', views.create_news, name="create_news"),

    path('<slug:catSlugName>', views.categoryList, name="categoryList"),
    path('news/<slug:BlogSlugName>', views.blogText, name="blogText"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

