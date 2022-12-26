class findName:
    preps = [['Широков', 'Андрей', 'Игоревич', '1'], ['Широков', 'Борис', 'Игоревич', '2'], ['Абрамова', 'Александра', 'Александровна', '3']]

    def __init__(self):
        pass

    def checkWord(self, word, allowTeachers):
        word = word.lower()
        word = word[:-2]
        newAllowTeachersList = []
        for teacher in allowTeachers:
            canChooseThisOne = False
            for name in teacher:
                name = name.lower()
                realName = name
                name = name[:len(word)]
                if (name == word and abs(len(realName) - len(word)) <= 2):
                    canChooseThisOne = True
            if (canChooseThisOne):
                newAllowTeachersList.append(teacher)

        if (len(newAllowTeachersList) == 0):
            newAllowTeachersList = allowTeachers
        return newAllowTeachersList

    def get(self, text):
        allowTeachers = self.preps
        text = text.split()
        for word in text:
            allowTeachers = self.checkWord(word, allowTeachers)
        return allowTeachers
