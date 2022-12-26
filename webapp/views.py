from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from webapp.models import RegisrationData
from webapp.utils.key_generator import *
from webapp.utils.eljur_auth import EljurAuth
from webapp.utils.time_helper import *

import time


def index(request):
    return render(request, 'index/index.html')


def testAlice(request):
    return render(request, 'test/test.html')


@require_POST
def generateKey(request):
    timeWhileKeyValid = 2.02 * 60 * 1000  # in millis (2 mins)

    # mainUrl = 'https://api.eljur.ru/api/auth/'
    # params = {
    #     'devkey': '8227490faaaa60bb94b7cb2f92eb08a4',
    #     'vendor': 'hselyceum',
    #     'out_format': 'json',
    #     'login': request.POST['login'],
    #     'password': request.POST['password'],
    # }
    # # https://api.eljur.ru/api/auth?login=parent&password=eljur2012
    # result = requests.post(mainUrl, params=params)
    # if (result.status_code != 200):
    #     result_json = {}
    #     result = result.json()
    #     result_json['ok'] = "False"
    #     result_json['error'] = result['response']['error']
    #     return JsonResponse(result_json)
    #
    # result = result.json()

    eljur_auth = EljurAuth(request.POST.get('login', None), request.POST.get('password', None))

    if (not eljur_auth.is_successful):
        return JsonResponse(eljur_auth.result_query)

    registered_users = RegisrationData.objects.filter(eljur_login=request.POST['login'])
    result_json = eljur_auth.result_query

    currentTime = get_current_time()

    RegisrationData.objects.filter(expires__lte=str(currentTime)).delete()

    if len(registered_users) == 0:
        expire_time = currentTime + timeWhileKeyValid
        result_json['key'] = generate_key()
        result_json['expire'] = expire_time
        result_text = result_json['key']
        result_text = result_text.lower()
        result_text = result_text.replace(',', '')
        result_text = result_text.replace(' ', '')
        new_regestration_data = RegisrationData(eljur_user_id=eljur_auth.eljur_id, eljur_login=eljur_auth.login,
                                              activation_phrase=result_text, expires=expire_time)
        new_regestration_data.save()
    else:
        result_json['key'] = registered_users[0].activation_phrase
        result_json['expire'] = registered_users[0].expires

    return JsonResponse(result_json)
