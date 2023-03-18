from django.urls import include, path

urlpatterns = [
    path('v1/', include('api.v1.users.urls')),
    path('v1/', include('api.v1.category_genres.urls')),
    path('v1/', include('api.v1.reviews_comments.urls')),
    path('v1/', include('api.v1.title.urls')),
]
