import nlpcloud


class My_API:
    def ner(self):
        para = input(self, 'enter the sentences: ')
        search_term = input('enter the search term: ')
        client = nlpcloud.Client('finetuned-gpt-neox-20b', '2be48590f743cc9181e20cb9c62cc2979d8646b1', gpu=True,
                                 lang='en'
                                 )
        response = client.entities(para, searched_entity=search_term)
        print(response)

    def lang_detection(self):
        para = input(self, 'enter the sentences: ')
        client = nlpcloud.Client("python-langdetect", "2be48590f743cc9181e20cb9c62cc2979d8646b1", gpu=False)
        response = client.langdetection(para)
        print(response)

    def sentiment_anlys(self, para):
        client = nlpcloud.Client("distilbert-base-uncased-emotion", "2be48590f743cc9181e20cb9c62cc2979d8646b1",
                                 gpu=False)
        response = client.sentiment(para)
        return response
