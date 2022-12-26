import requests

class EljurAuth():
    url = 'https://api.eljur.ru/api/auth/'
    params = {
        'devkey': '8227490faaaa60bb94b7cb2f92eb08a4',
        'vendor': 'hselyceum',
        'out_format': 'json',
    }

    result_query = dict()
    eljur_id = ""

    def __init__(self, login, password):
        self.params['login'] = login
        self.params['password'] = password
        self.login = login
        self.password = password

        result = requests.post(self.url, params=self.params)

        if result.status_code != 200:
            result = result.json()
            self.is_successful = False
            self.result_query['ok'] = "False"
            self.result_query['error'] = result['response']['error']

        else:
            result = result.json()
            self.is_successful = True
            self.eljur_id = result['response']['result']['token']
            self.result_query['ok'] = "True"

