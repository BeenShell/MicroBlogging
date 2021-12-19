from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views
from.views import about


urlpatterns = [
    path('', PostListView.as_view(), name='MemeOn-Home'), #If this is changed, remeber to change it in Base.Html in this line  # <a class="navbar-brand mr-4" href="/">Meme On 💭</a> #
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('memes/', views.memes, name='Memes-Home'),
    path('about/',views.about, name='About-Home'),

]
