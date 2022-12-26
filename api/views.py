from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponse, JsonResponse
from api.elements.text_parsing_helper import *


# Create your views here.

def index(request):
    return HttpResponse('HELLO, THAT\'S API')


@csrf_exempt
def reply_to_alice(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    try:
        response = {
            "version": data['version'],
            "session": {"session_id": data['session']['session_id'],
                        "message_id": data['session']['message_id'],
                        "user_id": data['session']['user_id'],
                        },
            "response": {
                "end_session": False
            }
        }
        response['response']['text'] = get_answer_alice(data['request']['command'], data['session']['user_id'],
                                                        data['session']['new'])
        response = json.dumps(response)
        return HttpResponse(response, content_type='application/json')
    except:
        return HttpResponse("Wrong data")


@csrf_exempt
def reply_to_ga(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    try:
        response = {
            'fulfillmentText': get_answer_ga(data['queryResult']['queryText'], data['originalDetectIntentRequest']['payload']['user']['userId'],
                                             data['queryResult']['intent']['displayName'], data['queryResult']['parameters']),
        }
        return JsonResponse(response)
    except:
        return HttpResponse("Wrong data", content_type='application/json')


@csrf_exempt
def reply_to_ga_test(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)

    # try:
    response = {
        "payload": {
            "google": {
                "expectUserResponse": True,
                "richResponse": {
                    "items": get_rich_answer_ga(data['queryResult']['queryText'], data['originalDetectIntentRequest']['payload']['user']['userId'],
                                                        data['queryResult']['intent']['displayName'], data['queryResult']['parameters']),
                    "suggestions": [
                        {
                            "title": "на сегодня"
                        },
                        {
                            "title": "на завтра"
                        }
                    ],
                }
            }
        },
    }
    print(response)
    return JsonResponse(response)
    # except:
    #     print("!ERROR")
    #     return HttpResponse("Wrong data", content_type='application/json')
