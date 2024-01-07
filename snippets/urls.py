# snippets/urls.py
from django.urls import path
from .views import snippet_list, create_snippet, share_snippet

urlpatterns = [
    path('list/', snippet_list, name='snippet_list'),
    path('create/', create_snippet, name='create_snippet'),
    path('share/<int:snippet_id>/', share_snippet, name='share_snippet'),
]
