from django.urls import path
from .views import home, about, post_request, PostDetailView


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('post_page/', post_request, name='post_page'),
    path('post_page/<int:pk>/', PostDetailView.as_view(), name='post_detail')
]