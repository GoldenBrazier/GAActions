from api.elements.textParsing.services.eljurApi import *
from api.elements.textParsing.services.eljurProcessing import *
from api.elements.textParsing.services.sendMessages import *
from api.elements.textParsing.classifier import *
from api.elements.textParsing.userData.activeUsers import *

classifier = Classifier()
eljur_api = EljurApi()
eljur_processing = EljurProcessing()
eljur_message_sender = SendMessages()


class RequestParsing:

    def _user_check_in(self, eljurId):
        if activeUsers.get(eljurId) is None:
            activeUsers.add(eljurId)

    def _proccess_dialog(self, eljur_id, is_end_dialog, module_name):
        if is_end_dialog:
            activeUsers.get(eljur_id).exitFromModule()
        else:
            activeUsers.get(eljur_id).activateModule(module_name)

    def _restore_module(self, eljur_id, standart_value):
        ask_module = standart_value
        if activeUsers.get(eljur_id).activeModule != None:
            ask_module = activeUsers.get(eljur_id).activeModule

        return ask_module

    def process(self, user_text, eljur_id, detect_module=None, ga_params=None):

        self._user_check_in(eljur_id)
        if detect_module == None:
            request_params = classifier.get(eljur_id, user_text)[0]
        else:
            request_params = {'class': detect_module, 'date': classifier.find_date(user_text),
                              'subject': classifier.find_subject(user_text)}

        if request_params.get('class') == 'other':
            if activeUsers.get(eljur_id).previus_module is not None:
                prev_params = activeUsers.get(eljur_id).previus_module
                print(prev_params)
                if prev_params.get('class') in ['homework', 'schedule', 'marks']:
                    is_updated_values = False
                    print(request_params)
                    if request_params.get('subject') is not None:
                        is_updated_values = True
                        prev_params['subject'] = request_params.get('subject')

                    if classifier.find_date("") == request_params.get('date'):
                        text_to_check = user_text.lower()
                        if text_to_check.find('сегодня') != -1 or text_to_check.find('сейчас') != -1:
                            is_updated_values = True
                            prev_params['date'] = request_params.get('date')
                    else:
                        is_updated_values = True
                        prev_params['date'] = request_params.get('date')

                    if is_updated_values:
                        request_params = prev_params

        active_module = self._restore_module(eljur_id, request_params.get('class'))
        print(request_params)

        # updarting history of requests
        activeUsers.get(eljur_id).previus_module = request_params

        if (active_module == 'homework'):
            result = eljur_api.process(eljur_id, 'gethomework', request_params.get('date'))
            if (result == 'Ошибка()'):
                return result
            answer, end_dialog = eljur_processing.processHomework(result, request_params.get('subject'))
            self._proccess_dialog(eljur_id, end_dialog, active_module)
            return answer

        elif (active_module == 'schedule'):
            result = eljur_api.process(eljur_id, 'getschedule', request_params.get('date'))
            if (result == 'Ошибка()'):
                return result
            answer, end_dialog = eljur_processing.processShedule(result)
            self._proccess_dialog(eljur_id, end_dialog, active_module)
            return answer

        elif (active_module == 'marks'):
            result = eljur_api.process(eljur_id, 'getmarks', request_params.get('date'))
            if (result == 'Ошибка()'):
                return result
            answer, end_dialog = eljur_processing.proccessMarks(result, request_params.get('subject'))
            self._proccess_dialog(eljur_id, end_dialog, active_module)
            return answer

        elif (active_module == 'skip lesson - yes'):
            result = eljur_api.process(eljur_id, 'getmessagereceivers')
            answer = eljur_processing.proccess_receivers(result)
            date = ""
            for d in ga_params['date']:
                date += d[:10] + ', '
            result = eljur_api.send_message(eljur_id, 'Отсутствие', 'Я буду отсутствовать ' + date, ['21534'])
            return result

        elif (active_module == 'other'):
            # TODO (FOR TEST ONLY)
            if request_params.get('generatedText') is None:
                return "Тут я бессилен"
            return request_params.get('generatedText')

        else:
            if request_params.get('generatedText') is None:
                return "Тут я бессилен"
            return request_params.get('generatedText')
