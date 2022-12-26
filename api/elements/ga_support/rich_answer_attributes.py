class gaRichAnswerAttributes:

    def createText(self, text, speech):
        return {
            "simpleResponse": {
                "textToSpeech": speech,
                "displayText": text
            }
        }

    def createTable(self, title, subtitle, columns_count, title_of_columns, data):
        tabel = {
            "tableCard": {
                "title": title,
                "subtitle": subtitle,
                "columnProperties": [],
                "rows": []
            }
        }

        for title_of_column in title_of_columns:
            current_title = {
                "header": title_of_column,
                "horizontalAlignment": "LEADING"
            }
            tabel['tableCard']['columnProperties'].append(current_title)

        for row_data in data:
            row = {
                "cells": [],
                "dividerAfter": False
            }
            for cell_data in row_data:
                cell = {
                    "text": cell_data
                }
                row["cells"].append(cell)

            tabel['tableCard']['rows'].append(row)

        return tabel
