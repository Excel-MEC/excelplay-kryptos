from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Level, KryptosUser
from api.serializers import LevelSerializer
from .decorators import is_logged_in, set_cookies


@set_cookies
@is_logged_in
def ask(request):

    user = request.session['user']
    kuser, created = KryptosUser.objects.get_or_create(user_id=user)
    # TODO: Send message to websocket on new user.
    level = Level.objects.filter(level=kuser.level)[0]
    serializer = LevelSerializer(level)
    return Response(serializer.data)


@is_logged_in
@api_view(['POST'])
def answer(request):
    answer = request.data['answer']

    try:
        user = request.session['user']
        kuser = KryptosUser.objects.get(user_id=user)
        level = Level.objects.get(level=kuser.level)

        if answer == level.answer:
            # Here we use an F expression : Read more about it in Django docs.
            kuser.level = F('level') + 1
            kuser.save()
            response = {'answer': 'Correct'}

        else:
            response = {'answer': 'Wrong'}

        return JsonResponse(response)

    except Exception as e:
        resp = {'Error': 'Internal Server Error'}
        return JsonResponse(resp, status=500)
