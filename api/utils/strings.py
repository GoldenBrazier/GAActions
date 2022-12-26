class Strings:
    result = dict()

    def __init__(self):
        self.result['retry_to_login'] = "Неправильные ключевые слова... Попробуйте еще раз!"
        self.result['new_user'] = "Привет, что бы продолжить работу войдите в систему"
        self.result['successful_login'] = "Добро пожаловать! Теперь Вам открыты все возможности."

    def get(self, input):
        return self.result.get(input, "#ERR: NO SUCH WORD")
