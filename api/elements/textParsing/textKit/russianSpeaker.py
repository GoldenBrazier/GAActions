import random


class RussianSpeaker:

    def datePrepare(self, weekday):
        weekday = weekday.lower()
        if weekday == 'понедельник':
            case = 'imenitelny'
        if weekday == 'вторник':
            case = 'imenitelny'
        if weekday == 'среда':
            case = 'vinitelny'
        if weekday == 'четверг':
            case = 'imenitelny'
        if weekday == 'пятница':
            case = 'vinitelny'
        if weekday == 'суббота':
            case = 'vinitelny'
        if weekday == 'воскресенье':
            case = 'imenitelny'

        if case == 'imenitelny':
            return weekday
        if case == 'vinitelny':
            return weekday[:-1] + 'у'

    def isGlagol(self, text):
        text = text.split()
        for i in text:
            if len(i) > 3:
                if i[-3:] == 'ать':
                    return True
                return False
        return False

    def removePunctuationMark(self, text):
        signs = set('.?,!;:')
        now = -1
        if not (text[now] == ' ' or text[now] in signs):
            return text

        while (text[now - 1] == ' ' or text[now - 1] in signs):
            now -= 1
        return text[:now]

    def getMarksCount(self, count):
        if count == 2:
            return 'две'
        if count == 3:
            return 'три'
        if count == 4:
            return 'четыре'
        if count == 5:
            return 'пять'
        if count == 6:
            return 'шесть'

    def getMarksSubtitle(self):
        startPhrases = ['За эту дату', 'В этот день', 'В тот день']
        nextword = ['Вы получили', 'Вам поставили', 'в дневнике стоят следующие оценки']
        return random.choice(startPhrases) + ' ' + random.choice(nextword) + ': '

    def getSheduleSubtitle(self, weekday):
        weekday = weekday.lower()
        nextword = ['будет', 'следующие предметы']
        firstWordVariants = ['В', 'Это']

        firstWord = random.choice(firstWordVariants)

        if weekday == 'вторник' and firstWord == 'В':
            firstWord += 'о'

        if firstWord == 'Это':
            nextword = ['вот что будет', 'вот расписание', 'ваши уроки']
            return firstWord + ' ' + weekday + ', ' + random.choice(nextword) + ': '

        return firstWord + ' ' + self.datePrepare(weekday) + ' ' + random.choice(nextword) + ': '

    def getHomeworkSubtitle(self, weekday):
        weekday = weekday.lower()
        nextword = ['задано', 'надо сделать следующие']
        prevWord = ['Домашнее задание', 'Задания', 'Вот что я нашел']
        firstWord = 'На'

        if (random.randint(0, 1) == 1):
            return firstWord + ' ' + self.datePrepare(weekday) + ' ' + random.choice(nextword) + ': '
        else:
            return random.choice(prevWord) + ' ' + firstWord.lower() + ' ' + self.datePrepare(weekday) + ': '

    def no_lessons(self):
        prevWord = ['Кажется, у Вас выходной', 'Нет уроков', 'Странно, я ничего не нашел', 'Уроков нет']
        return random.choice(prevWord)

    def no_homework(self):
        prevWord = ['Отдыхайте', 'Я ничего не нашел', 'Учителя ничего не задали', 'Нет задания', 'Нет задания, а Вы хотели?']
        return random.choice(prevWord)
