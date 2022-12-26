import requests

class EljurApi:

    def process(self, eljur_id, method, date="none"):
        mainUrl = 'https://api.eljur.ru/api/' + method
        params = {
            #8227490faaaa60bb94b7cb2f92eb08a4
            'devkey': '8227490faaaa60bb94b7cb2f92eb08a4',
            'auth_token': eljur_id,
            'days': date,
            'vendor': 'hselyceum',
            'out_format': 'json'
        }

        result = requests.get(mainUrl, params=params)

        if (result.status_code != 200):
            return "Ошибка()"

        result = result.json()
        return result

    def send_message(self, eljur_id, subject, text, addressees):
        mainUrl = 'https://api.eljur.ru/api/sendmessage'

        addressees_str = ""
        for addressee in addressees:
            addressees_str += addressee + ','
        addressees_str = addressees_str[:-1]

        params = {
            # 8227490faaaa60bb94b7cb2f92eb08a4
            'devkey': '8227490faaaa60bb94b7cb2f92eb08a4',
            'auth_token': eljur_id,
            'subject': subject,
            'text': text,
            'users_to': addressees_str,
            'vendor': 'hselyceum',
            'out_format': 'json'
        }

        result = requests.post(mainUrl, params=params)

        if (result.status_code != 200):
            return "Ошибка"
        else:
            return "Я всем сообщил"
