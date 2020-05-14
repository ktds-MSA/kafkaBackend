from django.urls import path, include

from . import controller

urlpatterns = [
    path('kafkatopics/<str:namespace>/<str:name>', controller.kafkatopic),
    path('kafkatopics/<str:namespace>/<str:name>/delete', controller.kafkatopicDelete),
    path('', include('swagger_ui.urls')),
]