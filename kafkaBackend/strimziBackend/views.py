from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    data = {'apiVersion': 'kafka.strimzi.io/v1beta1',
 'kind': 'KafkaTopic',
 'metadata': {'clusterName': '',
              'creationTimestamp': '2020-05-11T07:01:03Z',
              'generation': 1,
              'labels': {'strimzi.io/cluster': 'my-cluster'},
              'name': 'create-topic',
              'namespace': 'kafka',
              'resourceVersion': '405649',
              'selfLink': '/apis/kafka.strimzi.io/v1beta1/namespaces/kafka/kafkatopics/create-topic',
              'uid': '2d7ed9e6-9355-11ea-84b0-025000000001'},
 'spec': {'config': {'retention.ms': 7200000, 'segment.bytes': 1073741824},
          'partitions': 1,
          'replicas': 1}}
    return JsonResponse(data,json_dumps_params = {'ensure_ascii': True})
