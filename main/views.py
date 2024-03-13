from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from inmest_api.utils import *
from main.models import *
from main.serializers import *
import datetime
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


def json_response(request):
    return JsonResponse({"name": "Lucky"})

def say_hello(req):
    return HttpResponse("<h1>Hello Fleur</h1>")

def user_profile(request):
    return JsonResponse({
        "name": "TheOnlyBen",
        "email":"ben@gmail.com",
        "phone":"+243991735788"
        })


def filter_queries(request, id):
    query = {
        "id": id,
        "title": "Query",
        "description": "A test query",
        "status": "pending",
        "submitted_by": "Ben"
    }
        

    return JsonResponse(query)


class QueryView(View):
    queries = [
        {"id":1, "title":"Adama declined Val shots"},
        {"id":2, "title":"Samson declined Val shots"},
    ]
    def get(self, request):
        return JsonResponse({"result": self.queries})
    
    def post(self, request):
        return JsonResponse({"status": "ok"})


@api_view(['GET'])
def fetch_class_schedule(request):
    print("user making resquest", request.user)
    # 1. Retreive from DB all class schedules
    queryset = ClassSchedule.objects.all()

    # 2. Return queryset result as response
    # 2b. Transform/serialize queryset result to JSON and send as response

    serializer = ClassScheduleSerializer(queryset, many=True)

    return Response({'data': serializer.data}, status.HTTP_200_OK)

@api_view(['POST'])
def create_class_schedule(request):
    # 1. Get data from request (fronted)
    title = request.data.get('title')
    description = request.data.get('description')
    start_date_and_time = request.data.get('start_date_and_time')
    end_date_and_time = request.data.get('end_date_and_time')
    cohort_id = request.data.get('cohort_id')
    venue = request.data.get('venue')
    facilitator_id = request.data.get('facilitator_id')
    is_repeated = request.data.get('is_repeated')
    repeat_frequency = request.data.get('repeat_frequency')
    meeting_type = request.data.get('meeting_type')
    course_id = request.data.get('course_id')


    # Validations
    if not title:
        return Response({'error': 'Title is required'}, status.HTTP_400_BAD_REQUEST)

    cohort = None
    facilitator = None
    course = None

    #Validating the exitence of records
    try:
        cohort = Cohort.objects.get(id=cohort_id)

    except Cohort.DoesNotExist:
        return Response({'error': 'Cohort does not exist'}, status.HTTP_404_NOT_FOUND)
    try:
        facilitator = IMUser.objects.get(id=facilitator_id)

    except IMUser.DoesNotExist:
        return Response({'error': 'Facilitator does not exist'}, status.HTTP_404_NOT_FOUND)
    
    try:
        course = Course.objects.get(id=course_id)

    except Course.DoesNotExist:
        return Response({'error': 'Course does not exist'}, status.HTTP_404_NOT_FOUND)
    
    class_schedule = ClassSchedule.objects.create(
        title=title,
        description=description,
        venue=venue,
        is_repeated=is_repeated,
        repeat_frequency=repeat_frequency,
        start_date_and_time= datetime.datetime.now(),
        end_date_and_time= datetime.datetime.now(),
        facilitator=facilitator,
        cohort=cohort,
        course=course,
        organizer=facilitator,
    )
    class_schedule.save()
    serializer = ClassScheduleSerializer(class_schedule, many=False)

    return Response({'message': 'Schedule Successfully created', 'data': serializer.data}, status.HTTP_201_CREATED)



class QueryModelViewSet(viewsets.ModelViewSet):
    @action(detail=False, methods=['post'])
    def raise_query(self, request):
        title = request.data.get('title')
        description = request.data.get('description', None)
        query_type = request.data.get('query_type',None)
        assignee = None

        query = Query.objects.create(
            title=title,
            description=description,
            query_type=query_type,
            submitted_by=request.user
        )
        query.save()
        #send email to the assignee
        return Response({'message': 'Query successfully submitted'})
    
    @action(detail=False, methods=['post'])
    def filter_queries(self, request):
        search_text = request.data.get('search_text')
        status = request.data.get('status')
        paginator = PageNumberPagination()

        queryset = Query.objects.all()
        serializer = QuerySerializer(paginator.paginate_queryset(queryset, request), many=True)
        return paginator.get_paginated_response(serializer.data)
     
class ClassModelViewSet(viewsets.ModelViewSet):
    pass
