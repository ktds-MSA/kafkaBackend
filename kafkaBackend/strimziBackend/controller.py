from django.http import HttpResponse, request, JsonResponse

from .kafkaClass import KafkaTopic


def kafkatopicGet(request,namespace, name):
    if request.method == "GET":
        result = KafkaTopic(namespace).get(name)
        return JsonResponse(result)

def kafkatopicCreate(request, namespace, name):
    if request.method == "POST":
        result = KafkaTopic(namespace).create
        return JsonResponse(result)

def kafkatopicUpdate(request, namespace, name):
    if request.method == "POST":
        result = KafkaTopic(namespace).update()
        return JsonResponse(result)


def kafkatopicDelete(request,namespace, name):
    result = KafkaTopic(namespace).delete(name)
    return JsonResponse(result)