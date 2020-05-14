from django.http import HttpResponse, request, JsonResponse

from .kafkaClass import KafkaTopic


def kafkatopic(request,namespace, name):
    if request.method == "GET":
        result = KafkaTopic(namespace).get(name)
        return JsonResponse(result)
    elif request.method == "POST":
        return None

def kafkatopicDelete(request,namespace, name):
    result = KafkaTopic(namespace).delete(name)
    return JsonResponse(result)