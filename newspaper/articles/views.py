from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from articles.models import Article, Comment
# Create your views here.


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_details.html'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        article = self.get_object()
        if article.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'article_update.html'
    fields = ('title', 'body')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        article = self.get_object()
        if article.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_create.html'
    fields = ['comment']
    login_url = 'login'
    article = None

    def post(self, request, pk, **kwargs):
        self.article = get_object_or_404(Article, pk=pk)
        return super().post(request, pk, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = self.article
        return super().form_valid(form)
