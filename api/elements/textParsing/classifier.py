from api.elements.textParsing.textKit.findClassSbert import *
from api.elements.textParsing.textKit.findSubject import *
from api.elements.textParsing.textKit.findDate import *
from api.elements.textParsing.textKit.findName import *
from api.elements.textParsing.faqsKit.faqs import *
from api.elements.textParsing.userData.activeUsers import *

findDate = findDate()
findSubject = findSubject()
findClass = findClass()
findName = findName()
faqs = faqs()

class Classifier:
    MAX_ALLOW_SENTENCES_LEN = 52

    def getUserModule(self, userId):
        if (activeUsers.get(userId) != None):
            return activeUsers.get(userId).activeModule
        return None

    def setUserModule(self, userId, moduleName):
        if (activeUsers.get(userId) != None):
            activeUsers.get(userId).activeModule = moduleName

    def err_max_len(self):
        return ['Я еще не научился говорить об этом']

    def getAnswer(self, answers, quickAnswers):
        resultQuery = list()
        for answer in answers:
            curQuery = {}
            curQuery['answered'] = True
            curQuery['generatedText'] = answer
            resultQuery.append(curQuery)

        resultQuery[-1]['quickAnswers'] = quickAnswers
        return resultQuery

    def find_date(self, user_text):
        return findDate.get(user_text)

    def find_subject(self, user_text):
        return findSubject.get(user_text)

    def generate_answer(self, userId, userText):
        userText = str(userText)
        userText = userText[:52]
        classType = findClass.get(userText)

        botFAQS = faqs.get(userText)
        if botFAQS != None:
            return self.getAnswer([botFAQS], None)
        curQuery = {}
        curQuery['answered'] = False
        curQuery['class'] = classType
        curQuery['date'] = findDate.get(userText)
        curQuery['subject'] = findSubject.get(userText)
        curQuery['teacher'] = findName.get(userText)
        if (len(curQuery['teacher']) != 1):
            curQuery['teacher'] = None
        else:
            curQuery['teacher'] = curQuery['teacher'][0]
        return [curQuery]


    def get(self, userId, userText):
        return self.generate_answer(userId, userText)
