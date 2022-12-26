import os

class faqs:

    faqsData = {}
    current = os.path.dirname(os.path.realpath(__file__))
    data_path = current + "/data/faqs.txt"

    def delSign(self, s):
        delitable_sign = set('[]{}();:",.?!')
        for i in delitable_sign:
            s = s.replace(i, '')
        return s

    def read_data(self):
        with open(self.data_path, 'r', encoding='utf-8') as f:
            lines = f.read().split('\n')
        for line in lines:
            if (len(line) < 1):
                continue
            question, answer = line.split('?')
            question = self.delSign(question.lower())
            self.faqsData[question] = answer[1:]

    def __init__(self):
        self.read_data()

    def get(self, text):
        text = self.delSign(text.lower())
        return self.faqsData.get(text)
