from django.urls import include, path

urlpatterns = [
    path('api/', include('api.v1.urls')),
]
