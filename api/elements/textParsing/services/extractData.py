import requests
import json

class EljurExtractor:

    def exteactShedule(self, result):
        result = result['response']['result']
        if (len(result) == 0):
            return []
        result = result['students']
        resultText = ''
        resultDayData = {}
        for student in result.keys():
            student = result[student]
            for day in student['days'].keys():
                day = student['days'][day]
                resultDayData['title'] = day['title']
                resultDayData['subjects'] = []
                previusSubject = 'none'
                countOfSubject = 0
                for subject in day['items'].keys():
                    subject = day['items'][subject]

                    resultSubject = {
                        'title': subject['name'],
                        'time': "9:30"
                    }

                    resultDayData['subjects'].append(resultSubject)

        return [resultDayData]

    def processHomework(self, result, requestedSubject):
        result = result['response']['result']
        if (len(result) == 0):
            return (russianSpeaker.no_homework(), True)
        result = result['students']
        result_text = ''

        allSubject = True
        if (requestedSubject != None):
            allSubject = False
            resSub = []
            for sub in requestedSubject:
                resSub.append(sub)
            requestedSubject = resSub

        for student in result.keys():
            student = result[student]
            for day in student['days'].keys():
                day = student['days'][day]
                result_text += russianSpeaker.getHomeworkSubtitle(day['title'])
                for subject in day['items'].keys():
                    subject = day['items'][subject]
                    if (allSubject or (subject['name'] in requestedSubject)):
                        result_text += 'по предмету ' + subject['name'].lower()
                        firstText = True
                        for task in subject['homework'].keys():
                            task = subject['homework'][task]
                            if firstText:
                                if russianSpeaker.isGlagol(task['value']):
                                    result_text += ' надо '
                                else:
                                    result_text += ' задано: '
                            result_text += russianSpeaker.removePunctuationMark(task['value']).lower() + ', '
                            firstText = False
                            result_text = result_text[:-2]
                    result_text += '; '
        return (result_text[:-2], True)

    def proccessMarks(self, result, requestedSubject):
        result = result['response']['result']
        if (len(result) == 0):
            return ('Нет отметок за эту дату', True)
        result = result['students']
        resultText = ''

        allSubject = True
        if (requestedSubject != None):
            allSubject = False
            resSub = []
            for sub in requestedSubject:
                resSub.append(sub)
            requestedSubject = resSub

        for student in result.keys():
            student = result[student]
            startPhrase = russianSpeaker.getMarksSubtitle()
            resultText += startPhrase
            for lessons in student['lessons']:
                if allSubject or (lessons['name'] in requestedSubject):
                    added = False
                    allMarks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    for marks in lessons['marks']:
                        if (marks['value'] != 'н'):
                            added = True
                            allMarks[int(marks['value'])] += 1

                    for mark, count in enumerate(allMarks):
                        if count > 1:
                            resultText += russianSpeaker.getMarksCount(count) + ' "' +str(mark) + '", '
                        if count == 1:
                            resultText += '"' +str(mark) + '", '

                    if added:
                        resultText = resultText[:-2] + ' по предмету ' + lessons['name'].lower() + '; '

        if (resultText == startPhrase):
            resultText = 'У Вас нет оценок за это число '

        return (resultText[:-1], True)

    def proccessFAQS(self, userText):
        needScoreToShow = 70
        url = 'https://westus.api.cognitive.microsoft.com/qnamaker/v2.0/knowledgebases/1df2ec54-c653-44c3-9fc3-33fbef695b44/generateAnswer'
        payload = {
            'question': userText,
            'top': '1',
        }
        headers = {
            'Ocp-Apim-Subscription-Key': '558d2204992b4a59bba419e98bd2d39d',
            'Content-Type': 'application/json'
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        r = r.json()
        print(r)
        if (int(r['answers'][0]['score']) >= needScoreToShow):
            return (r['answers'][0]['answer'], True)
        else:
            return ("Search our website", True)

    def proccess_receivers(self, result, with_param=None):
        result = result['response']['result']['groups']
        answer = []
        for student in result:
            if with_param is None or student['key'] == with_param:
                answer += student['users']

        print(answer)
        return answer
