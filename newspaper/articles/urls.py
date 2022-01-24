from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_details'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('', ArticleListView.as_view(), name='article_list'),

]
