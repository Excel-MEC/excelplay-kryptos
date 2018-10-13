from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Level, KryptosUser
from api.serializers import LevelSerializer
from .decorators import is_logged_in, set_cookies


@is_logged_in
@api_view(['GET'])
def ask(request):

    # TODO: Fetch user level from DB
    user_level = 2
    level = Level.objects.filter(level=user_level)[0]
    serializer = LevelSerializer(level)
    return Response(serializer.data)

    # response = {
    #     'level': user_level,
    #     'source_hint': level.source_hint,
    #     'level_file': level.level_file,
    # }
    # return JsonResponse(response)

@csrf_exempt
@api_view(['POST'])
def answer(request):
    user_id = request.data['user_id']
    answer = request.data['answer']
    try:
        user = User.objects.get(user_id=user_id)
        kuser = KryptosUser.objects.get(user_id=user)
        level = Level.objects.get(level=kuser.level)
        if answer == level.answer:
            print(user, " answered level ", kuser.level, " correctly.")
            kuser.level += 1
            kuser.save()
            response = {'answer': 'Correct'}
        else:
            response = {'answer': 'Wrong'}
    except Exception as e:
        print (e)
        response = {'error': 'User not found'}
    finally:
        return JsonResponse(response)
