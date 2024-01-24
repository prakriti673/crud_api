from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt


# if using class-based views import these
# from django.utils.decorators import method_decorator
# from django.views import View
# @method_decorator(csrf_exempt, name='dispatch')
# class StudentAPI(View):
    # def get(self,request,*args,**kwargs):
    #    same..... 
    # def post(self,.....):
    #     same...
    # def put(self,...)
    #     ....


@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        # --  flow  --
        # json->byte stream of data->python data->complex data(model instance)
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    #if user wants to create a field in the Student table
    if request.method == 'POST':
        json_data = request.body 
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')


    # if user want to update a field in the Student table
    if request.method == 'PUT':
        json_data = request.body 
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        # if we want to do complete update, Partial=True is not required
        # to change only some fields, partial=True is required
        serializer = StudentSerializer(stu,data = pythondata, partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')


    if request.method =='DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data deleted'}
        # instead of these 2 lines, we can use JsonResponse 
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type='application/json')
        
        return JsonResponse(res, safe=False)

            