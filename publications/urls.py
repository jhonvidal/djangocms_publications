from django.conf.urls import *
from .views import PubPostListView, PubPostDetailView, TaggedListView, CategoryListView

urlpatterns = patterns('',
                       url(r'^$', PubPostListView.as_view(), name='post_list'),
                       url(r'^(?P<slug>[-\w]+)/$', PubPostDetailView.as_view(), name='post_detail'),
                       url(r'^tag/(?P<tag>[-\w]+)/$', TaggedListView.as_view(), name='posts_tagged'),
                       url(r'^category/(?P<category>[-\w]+)/$', CategoryListView.as_view(), name='posts_category'),
                       )
