from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import run_etl_task

class SyncView(APIView):
    def post(self, request):
        run_etl_task.delay()  # Trigger the Celery task asynchronously
        return Response({"message": "Synchronization task has been started!"}, status=status.HTTP_202_ACCEPTED)
