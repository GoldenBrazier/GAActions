from api.elements.textParsing.requestParsing import *
from api.elements.textParsing.richAnswerGA import *
from webapp.models import UserData
from webapp.models import RegisrationData
from webapp.utils.time_helper import *
from api.utils.strings import Strings
from api.elements.textParsing.textKit.findDate import *
from api.elements.ga_support.rich_answer_attributes import *

requestParsing = RequestParsing()
rich_request_parsing = RichRequestParsing()
strings = Strings()
date = findDate()
ga_attributes = gaRichAnswerAttributes()


def get_answer_alice(user_text, userId, newSession=False):
    if newSession == True:
        return strings.get('new_user')

    user = UserData.objects.filter(yandex_user_id=userId)

    if (len(user) == 0):
        return register_user(user_text, userId)

    else:
        return requestParsing.process(user_text, user[0].eljur_user_id)


def get_answer_ga(user_text, userId, detect_module, ga_params):
    user = UserData.objects.filter(yandex_user_id=userId)

    if (len(user) == 0):
        return register_user(user_text, userId)

    else:
        return requestParsing.process(user_text, user[0].eljur_user_id, detect_module, ga_params)


def get_rich_answer_ga(user_text, userId, detect_module, ga_params):
    user = UserData.objects.filter(yandex_user_id=userId)

    if (len(user) == 0):
        text = register_user(user_text, userId)
        resultArr = []
        resultArr.append(ga_attributes.createText(text, text))
        return resultArr

    else:
        return rich_request_parsing.process(user_text, user[0].eljur_user_id, detect_module, ga_params)

def register_user(user_text, userId):
    user_text = user_text.lower()
    user_text = user_text.replace(',', '')
    user_text = user_text.replace(' ', '')

    currentTime = get_current_time()

    RegisrationData.objects.filter(expires__lte=str(currentTime)).delete()
    regisration_user_data = RegisrationData.objects.filter(activation_phrase=user_text)

    if (len(regisration_user_data) == 0):
        return strings.get('retry_to_login')

    regisration_user_data = regisration_user_data[0]
    newUser = UserData(yandex_user_id=userId, eljur_user_id=regisration_user_data.eljur_user_id)
    newUser.save()
    return strings.get('successful_login')
