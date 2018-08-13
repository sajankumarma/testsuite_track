# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from . import zookeeper
from django.shortcuts import render


# Create your views here.
def index(request):
    is_up=zookeeper.zookeeper().is_zk_up('10.71.67.159','6789')
    if is_up==True:
        return HttpResponse("zookeeper is up")
    else:
        return HttpResponse("zookeeper is down")

