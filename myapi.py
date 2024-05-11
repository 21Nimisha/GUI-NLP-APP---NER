import textrazor

class TextRazorAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        textrazor.api_key = api_key

    def entity_recognition(self, text):
        client = textrazor.TextRazor(extractors=["entities"])
        response = client.analyze(text)
        entities = [entity for entity in response.entities()]
        return entities

