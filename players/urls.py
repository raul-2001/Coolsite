from django.urls import path
from players.views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', PlayersHome.as_view(), name='home'),
    # path('category/<int:cat_id>/', show_category, name='category'),
    path('category/<slug:cat_slug>/', PlayersCategory.as_view(), name='category'),
    # path('post/<slug:post_slug>/', show_post, name='post'),
    path('post/<slug:post_slug>/', PlayerShowPost.as_view(), name='post'),
    path('about/', about, name='about'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('feedback/', feedback, name='feedback'),
    # path('add_post/', add_post, name='add_post'),
    path('add_post/', PlayerAddPost.as_view(), name='add_post'),
]