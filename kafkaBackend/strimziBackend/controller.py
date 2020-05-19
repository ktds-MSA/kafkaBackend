from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .kafkaClass import KafkaTopic

def kafkatopicGet(request,context, namespace, name):

    if request.method == "GET":
        result = KafkaTopic(context,namespace).get(name)
        return JsonResponse(result)

@csrf_exempt
def kafkatopicCreate(request, context, namespace, name):
    if request.method == "POST":
        received_json_data = json.loads(request.body)
        result = KafkaTopic(context,namespace).create(name, received_json_data['namespace'], received_json_data['cluster'], received_json_data['partition'],received_json_data['replicas'])
        return JsonResponse(result)

@csrf_exempt
def kafkatopicUpdate(request, context, namespace, name):
    if request.method == "POST":
        result = KafkaTopic(context, namespace).update(name)
        return JsonResponse(result)

@csrf_exempt
def kafkatopicDelete(request,context, namespace, name):
    if request.method == "POST":
        result = KafkaTopic(context, namespace).delete(name)
        return JsonResponse(result)