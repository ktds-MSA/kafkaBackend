import json
from abc import *
from string import Template

from kubernetes.client.rest import ApiException
from kubernetes import client, config
from pprint import pprint
import kubernetes

class Strimzi(metaclass=ABCMeta):
    _template = ''
    _group = ''
    _version = ''
    _namespace = ''
    _plural = ''
    _body = ''
    _name = ''

    def __init__(self, context, namespace):
        pass

    @abstractmethod
    def get(self, name):
        pass

    @abstractmethod
    def create(self, name):
        pass

    @abstractmethod
    def update(self, name):
        pass

    @abstractmethod
    def delete(self, name):
        pass

    def templateRender(self,*args, **kwargs):
        templateInstance = Template(self._template)
        tempStr = templateInstance.substitute(*args,**kwargs)
        return json.loads(tempStr)



class KafkaTopic(Strimzi):
    """
    Kafka  topic class
    """
    """
    Template Engine을 사용하기 위하여 template은 string 포멧을 사용한다.
    caution: string 안에 값
        int 형식일 경우는 ${var}식으로 감싸지 않고
        string 형식일 경우는 "${var}식으로 "" 쌍따옴표로 감싸야 된다.
        ex) '{"name":"feel", "namespace":"${namespace}"}'
    치환될 변수는 $ 달러 표시로 변수 임을 명시한다. 
    """

    _template ="""{
            "apiVersion": "kafka.strimzi.io/v1beta1",
            "kind": "KafkaTopic",
            "metadata": {
                "name": "${name}",
                "labels": {
                    "strimzi.io/cluster": "${cluster}"
                }
            },
            "spec": {
                "partitions":${partitions},
                "replicas": ${replicas},
                "config": {
                    "retention.ms": 7200000,
                    "segment.bytes": 1073741824
                }
            }
        }"""
    _group = 'kafka.strimzi.io'
    _version = 'v1beta1'
    _namespace = ''
    _plural = 'kafkatopics'
    _body = ''
    _name = ''
    _client = None

    def __init__(self, context, namespace):
        self._namespace = namespace
        # set kubernetes client
        config.load_kube_config()
        config.new_client_from_config(context=context)
        self._client = client.CustomObjectsApi()


    def get(self, name):
        try:
            api_response = self._client.get_namespaced_custom_object(self._group, self._version, self._namespace,
                                                                 self._plural, name)
        except ApiException as e:
            print("Exception during get kafka topics %s\n" % e)
            api_response = {"errorCode": str(e)}
        return api_response

    def create(self, name):
        # make body from template
        try:
            self._body = self.templateRender(name=name,namespace="kafka",cluster="my-cluster",partitions=2,replicas=1)
            api_response = self._client.create_namespaced_custom_object(self._group, self._version, self._namespace, self._plural, self._body)
        except ApiException as e:
            print("Exception during create kafka topics %s\n" % e)
            api_response = {"errorCode": str(e)}
        # update need to get and change values
        return api_response

    def update(self, name):
        # make body from template
        try:
            self._body = self.templateRender(name="maked-topic",namespace="kafka",cluster="my-cluster",partitions=2,replicas=1)
            api_response = self._client.create_namespaced_custom_object(self._group, self._version, self._namespace, self._plural, self._body)
        except ApiException as e:
            print("Exception during update kafka topics %s\n" % e)
            api_response = {"errorCode": str(e)}
        # update need to get and change values
        return api_response

    def delete(self, name):
        try:
            api_response = self._client.delete_namespaced_custom_object(self._group, self._version, self._namespace, self._plural, name)
        except ApiException as e:
            print("Exception during delete kafka topics %s\n" % e)
            api_response = {"errorCode": str(e)}
        return api_response
