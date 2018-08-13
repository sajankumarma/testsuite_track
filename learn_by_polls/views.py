# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from . import zookeeper
from . import kafka
from django.shortcuts import render


# Create your views here.
def index(request):
    is_up=zookeeper.zookeeper().is_zk_up('10.71.67.159','6789')
    if is_up==True:
        return HttpResponse("zookeeper is up and  "+ temp_kafka('10.71.67.159','6789'))
    else:
        return HttpResponse("zookeeper is down")

def temp_kafka(host,port):
    state,value=kafka.kafka().is_kafka_up(host,port)
    if state==True:
        return "kafka is up , brokers are "+value
    else:
        return "kafka is down"
