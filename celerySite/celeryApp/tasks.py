
from celerySite.celery import app
from celeryApp.models import SquareNumber


@app.task()
def check_square():
    sq_requests = SquareNumber.objects.filter(status__exact="PENDING")
    for sq_request in sq_requests:
        run_square.s(sq_request.id, sq_request.number).apply_async()


@app.task()
def run_square(sid, snum):
    sq_result = snum * snum
    sq_request = SquareNumber.objects.get(id=sid)
    sq_request.number = snum
    sq_request.square_number = sq_result
    sq_request.status = "COMPLETE"
    sq_request.save()
