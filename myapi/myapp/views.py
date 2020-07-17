from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from myapp.models import Student
@csrf_exempt
def index(request):
    all=list(Student.objects.values())
    return JsonResponse(all,safe=False)
@csrf_exempt
def get_student(request, idi):
    if request.method == 'GET':
        try:
            student = Student.objects.get(student_id=idi)
            response = json.dumps([{ 'Student_id': student.student_id, 'Name': student.name,'Standard':student.standard}])
        except:
            response = json.dumps([{ 'Error': 'No student with that name'}])
    
    if request.method == 'DELETE':
        try:
            student = Student.objects.get(student_id=idi)
            student.delete()
            response = json.dumps([{ 'Student': idi,"Update": ' Student is successfully deleted' }])
        except:
            response = json.dumps([{ 'Error': 'No student with this id.Please enter a valid id'}])
    if request.method == 'PUT':
        try:
            student1 = Student.objects.get(student_id=idi)
            student1.delete()
        except:
            response = json.dumps([{ 'Error': 'No student with that id'}])
            return HttpResponse(response, content_type='text/json')
        payload = json.loads(request.body)
        idi = payload['student_id']
        name = payload['name']
        standard=payload['standard']
        student = Student(student_id=idi, name=name,standard=standard)
        try:
            student.save()
            response = json.dumps([{ 'Success': 'Student updated successfully!'}])
        except:
            response = json.dumps([{ 'Error': 'Student could not be updated!'}])    

    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_student(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        id = payload['student_id']
        name = payload['name']
        standard = payload['standard']
        student = Student(student_id=id, name=name,standard=standard)
        try:
            student.save()
            response = json.dumps([{ 'Success': 'Student added successfully!'}])
        except:
            response = json.dumps([{ 'Error': 'Student could not be added!'}])
    return HttpResponse(response, content_type='text/json')




