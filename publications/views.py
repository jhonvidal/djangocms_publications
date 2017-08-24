# Import Generic Views
from django.views.generic import ListView, DetailView

# import Models
from .models import Post

# import Settings
from django.conf import settings


class PubPostListView(ListView):
    model = Post
    template_name = 'publications/pub_post_list.html'
    paginate_by = settings.PUB_PAGINATION
    context_object_name = 'post_list'

    def get_queryset(self):
        qs = super(PubPostListView, self).get_queryset()
        return qs.filter(is_publish=True)

    def get_context_data(self, **kwargs):
        context = super(PubPostListView, self).get_context_data(**kwargs)
        context['TRUNCWORDS_COUNT'] = settings.POSTS_LIST_TRUNCWORDS_COUNT

        return context


class PubPostDetailView(DetailView):
    model = Post
    template_name = 'publications/pub_post_detail.html'
    context_object_name = 'post'


class TaggedListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'publications/pub_post_list.html'
    paginate_by = settings.PUB_PAGINATION
    view_url_name = 'publications:posts_tagged'

    def get_queryset(self):
        qs = super(TaggedListView, self).get_queryset()
        return qs.filter(tags__slug=self.kwargs['tag'], is_publish=True)

    def get_context_data(self, **kwargs):
        kwargs['tagged_entries'] = (self.kwargs.get('tag')
                                    if 'tag' in self.kwargs else None)
        context = super(TaggedListView, self).get_context_data(**kwargs)
        context['TRUNCWORDS_COUNT'] = settings.POSTS_LIST_TRUNCWORDS_COUNT

        return context


class CategoryListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'publications/pub_post_list.html'
    paginate_by = settings.PUB_PAGINATION
    view_url_name = 'publications:posts_category'

    def get_queryset(self):
        qs = super(CategoryListView, self).get_queryset()
        return qs.filter(categories__slug=self.kwargs['category'], is_publish=True)

    def get_context_data(self, **kwargs):
        kwargs['category'] = (self.kwargs.get('category')
                              if 'category' in self.kwargs else None)
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['TRUNCWORDS_COUNT'] = settings.POSTS_LIST_TRUNCWORDS_COUNT

        return context
