#!/bin/bash
# request kafkaTopic post
curl -X POST -d @createData.dat http://127.0.0.1:8000/strimziBackend/kafkatopics/master-console-ktdscoe/kafka/my-topic/create
