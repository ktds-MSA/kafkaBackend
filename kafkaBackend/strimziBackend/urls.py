from django.urls import path, include

from . import controller

urlpatterns = [
    path('kafkatopics/<str:context>/<str:namespace>/<str:name>', controller.kafkatopicGet),
    path('kafkatopics/<str:context>/<str:namespace>/<str:name>/create', controller.kafkatopicCreate),
    path('kafkatopics/<str:context>/<str:namespace>/<str:name>/update', controller.kafkatopicUpdate),
    path('kafkatopics/<str:context>/<str:namespace>/<str:name>/delete', controller.kafkatopicDelete),
]