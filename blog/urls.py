from django.urls import path
from . import views
from django.conf import settings
from django.views import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

if settings.DEBUG:
    urlpatterns = (
        [
            path(
                "media/<path:path>/",
                static.serve,
                {"document_root": settings.MEDIA_ROOT, "show_indexes": True},
            ),
        ]
        + staticfiles_urlpatterns()
        + urlpatterns
    )