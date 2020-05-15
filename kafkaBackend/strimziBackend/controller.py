from django.http import HttpResponse, request, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .kafkaClass import KafkaTopic

def kafkatopicGet(request,namespace, name):
    if request.method == "GET":
        result = KafkaTopic(namespace).get(name)
        return JsonResponse(result)

@csrf_exempt
def kafkatopicCreate(request, namespace, name):
    if request.method == "POST":
        result = KafkaTopic(namespace).create(name)
        return JsonResponse(result)

@csrf_exempt
def kafkatopicUpdate(request, namespace, name):
    if request.method == "POST":
        result = KafkaTopic(namespace).update(name)
        return JsonResponse(result)

@csrf_exempt
def kafkatopicDelete(request,namespace, name):
    if request.method == "POST":
        result = KafkaTopic(namespace).delete(name)
        return JsonResponse(result)