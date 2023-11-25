from django.shortcuts import render
from django.http import HttpResponse
from celeryApp.models import SquareNumber
from celeryApp.tasks import run_square
from celerySite.celery import app as celery_app
import time


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the index file.</h1>")


def set_square(request, snum):

    sq_request = SquareNumber(number=snum, status="PENDING")
    sq_request.save()

    return HttpResponse("<h1> You're request of number {} is saved in ID : {}".format(snum, sq_request.id))


def get_square(request, sid):
    http_res = "<h1>Request hasnt been served. Please wait </h1>"
    res = SquareNumber.objects.get(id=sid)

    http_res = "<h1>The last result for square of {0} is {1}</h1>".format(res.number, res.square_number)
    return HttpResponse(http_res)
