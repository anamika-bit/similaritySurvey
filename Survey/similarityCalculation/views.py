from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Survey,similarityScore
from .serializers import SurveySerializer,similarityScoreSerializer
import json


class surveyView(APIView):
    def post(self,request):
        try:
            user_data = request.data
            serializer = SurveySerializer(data=user_data)
            if(serializer.is_valid()):
                serializer.save()
                return HttpResponse(serializer.data, content_type = 'application/json' ,status = 200)
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


class similarityScoreView(APIView):
    def post(self,request):
        try:
            id = request.data['id']
            curr_user = Survey.objects.get(id=id)
            serializer = SurveySerializer(curr_user,many=False)
            user = serializer.data
            queryset = Survey.objects.filter(~Q(id=id)).values()
            List = []
            for query in queryset:
                cnt=0
                for key in user:
                    if user[key] == query[key] and query[key]!='' and user[key]!='':
                        cnt = cnt+1
                similarity_score = cnt*5
                result = {
                    "user1" : user['id'],
                    "user1Name" : user['name'],
                    "user2": query['id'],
                    "user2Name" : query['name'],
                    "similarity_score" : f"{similarity_score}"
                }
                print("1")
                serializer2 = similarityScoreSerializer(data=result)
                print("2")
                similarityScore.save(result)
                if serializer2.is_valid():
                    serializer2.save()
                    print("3")
                    print(serializer2.data)
                    List.append(serializer2.data)
            return HttpResponse(json.dumps({"status":"success","message":List}), content_type = 'application/json' ,status = 200)

        except Exception as e:
            return HttpResponse(json.dumps({"status":"fail","message":str(e)}), content_type = 'application/json' ,status = 400)


    def get(self,request):
        try:
            name = request.GET.get('name','')
            page_size = 5
            page_number = 1
            queryset = []
            if name:
                queryset = similarityScore.objects.filter(Q(user1Name__icontains=name) & Q(user2Name__icontains=name)).values()
            else:
                queryset = similarityScore.objects.all().values()
            print(queryset)
            paginator = Paginator(queryset,page_size)
            page_obj = paginator.page(page_number)
            data = page_obj.object_list
            serializer = similarityScoreSerializer(data,many=True)
            return HttpResponse(json.dumps(serializer.data), content_type = 'application/json' ,status = 200)
        except Exception as e:
            return HttpResponse(json.dumps({"status":"fail","message":str(e)}), content_type = 'application/json' ,status = 400)


