from django.conf.urls import url, patterns

from forum.feeds import TopicsFeed,PostsFeed,ForumTopicsFeed,ForumPostsFeed,TopicPostsFeed


urlpatterns = [
    #Forum feeds
    url(r'^topics/$', TopicsFeed(), name='topics_feed'),
    url(r'^posts/$', PostsFeed(), name='posts_feed'),
    url(r'^forum_topics/(?P<forum_id>\d+)/$', ForumTopicsFeed(), name='forum_topics_feed'),
    url(r'^forum_posts/(?P<forum_id>\d+)/$', ForumPostsFeed(), name='forum_posts_feed'),
    url(r'^topic_posts/(?P<topic_id>\d+)/$', TopicPostsFeed(), name='topic_posts_feed'),
]
