import parsedatetime as pdt  # $ pip install parsedatetime pyicu
import time
from datetime import datetime, timedelta


class findDate:
    calendar = 0

    def __init__(self):
        self.calendar = pdt.Calendar(pdt.Constants(localeID='ru_RU'))

    def get_current_date(self):
        datetime_obj = self.calendar.parse()
        current_date = str(datetime_obj[0].tm_year) + self.processNum(datetime_obj[0].tm_mon) + self.processNum(
            datetime_obj[0].tm_mday)

        return current_date


    def get_month_date(self, text):
        text_arr = text.split()

        for ind, word in enumerate(text_arr):
            if (word == 'неделю'):
                if (ind - 1 >= 0):
                    prev_word = text_arr[ind - 1]
                    if (prev_word[:4] == 'пред'):
                        return 'prev_week'

                    elif (prev_word[:4] == 'след'):
                        return 'next_week'

                    else:
                        return 'this_week'

        return None

    def get_day_date(self, text):
        text_arr = text.split()

        data = {}
        data['Monday'] = ['понедельник', 'понедельника', 'понедельнику', 'понедельником', 'понедельнике', 'пн']
        data['Tuesday'] = ['вторник', 'вторника', 'вторнику', 'вторнике', 'вторником', 'вт']
        data['Wednesday'] = ['среда', 'среды', 'среде', 'среду', 'средой', 'ср']
        data['Thursday'] = ['четверг', 'четверга', 'четвергу', 'четверге', 'четвергом', 'чт']
        data['Friday'] = ['пятница', 'пятницы', 'пятнице', 'пятницу', 'пятницей', 'пт']
        data['Saturday'] = ['суббота', 'субботы', 'субботе', 'субботу', 'субботой', 'сб']
        data['Sunday'] = ['воскресенье', 'воскресенья', 'воскресенью', 'воскресеньем', 'вс']
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        lastDay = ""
        current_date = datetime.now()
        currentDay = current_date.strftime('%A')

        for ind, word in enumerate(text_arr):
            for day in data:
                dayTitle = day
                day = data[day]
                if word in day:
                    lastDay = dayTitle

        print(lastDay)
        if lastDay != "":
            needDay = week.index(lastDay)
            curDay = week.index(currentDay)

            if needDay < curDay:
                needDay += 7

            resultDate = datetime.today() + timedelta(days=(needDay - curDay))
            resStr = resultDate.strftime("%Y%m%d")
            return resStr

        return None

    def objctToDays(self, datetime_obj):
        return int(datetime_obj[0].tm_year * 365 + datetime_obj[0].tm_mon * 31 + datetime_obj[0].tm_mday)

    def processNum(self, num):
        if (num < 10):
            return '0' + str(num)
        return str(num)

    def get(self, text):
        if (self.get_month_date(text) != None):
            return self.get_month_date(text)

        if (self.get_day_date(text) != None):
            return self.get_day_date(text)

        datetime_obj = self.calendar.parse(text)
        currentTime = self.calendar.parse("")
        current_date = 0

        if (self.objctToDays(datetime_obj) - self.objctToDays(currentTime) > 40):
            current_date = str(datetime_obj[0].tm_year - 1) + self.processNum(datetime_obj[0].tm_mon) + self.processNum(
                datetime_obj[0].tm_mday)
        else:
            current_date = str(datetime_obj[0].tm_year) + self.processNum(datetime_obj[0].tm_mon) + self.processNum(
                datetime_obj[0].tm_mday)

        return current_date
