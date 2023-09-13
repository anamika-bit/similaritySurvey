from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Survey
from .serializers import SurveySerializer
import json
# Create your views here.

class surveyView(APIView):
    def post(self,request):
        try:
            serializer = SurveySerializer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return HttpResponse(json.dumps(serializer.data), content_type = 'application/json' ,status = 200)
            return HttpResponse(json.dumps({"status":"fail","message":"Something went wrong"}), content_type = 'application/json' ,status = 400)

        except Exception as e:
            return HttpResponse(json.dumps({"status":"fail","message":str(e)}), content_type = 'application/json' ,status = 400)

    def get(self,request):
        try:
            surveys = Survey.objects.all()
            serializer = SurveySerializer(surveys,many=True)
            return HttpResponse(json.dumps(serializer.data), content_type = 'application/json' ,status = 200)

        except Exception as e:
            return HttpResponse(json.dumps({"status":"fail","message":str(e)}), content_type = 'application/json' ,status = 400)

