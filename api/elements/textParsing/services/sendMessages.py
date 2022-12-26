from api.elements.textParsing.textKit.findName import *

findName = findName()

class SendMessages:
    usersData = {}

    def get(self, userId, userData, userText):
        currentStep = 0
        previusText = ""
        if (self.usersData.get(userId) != None):
            currentStep, previusText = self.usersData.get(userId)

        if (currentStep == 0):
            newData = findName.get(previusText + userText)
            if (len(newData) != 1):
                return ('Нет данных по учителю', False)
            self.usersData[userId] = (1, userText)
            return ('Продиктуйте текст', False)

        if (currentStep == 1):
            self.usersData[userId] = (2, userText)
            return ('Вы уверены что хотите отправить?', False)

        if (currentStep == 2):
            if (userText == 'да'):
                self.usersData[userId] = None
                return ('Ок', True)
            if (userText == 'нет'):
                self.usersData[userId] = None
                return ('Отменено', True)

            return ('Не понятно', False)
