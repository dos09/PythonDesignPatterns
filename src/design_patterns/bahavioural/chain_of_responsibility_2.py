"""
Chain of handlers, the first that can handle the request is
handling it, otherwise passes it to the next handler

Example:
    Pass a piece of text in unknown language to bunch of translators,
    the first one that can translate the text will do it.
    (T = translator)
    T1 -> T2 -> T3 ...
"""


class Response:

    def __init__(self, err_msg=None, data=None):
        self.err_msg = err_msg
        self.data = data

    def __str__(self):
        return 'ERR: %s, DATA: %s' % (self.err_msg, self.data)


class Translator:

    def __init__(self):
        self.next_translator = None

    def translate(self, text):
        return Response(err_msg='Can not translate the text')


class SumerianTranslator(Translator):

    def translate(self, text):
        if 'sumerian' in text:
            return Response(data='translated sumerian text')

        return self.next_translator.translate(text)


class HurrianTranslator(Translator):

    def translate(self, text):
        if 'hurrian' in text:
            return Response(data='translated hurrian text')

        return self.next_translator.translate(text)


def _get_translator():
    sumerian = SumerianTranslator()
    hurrian = HurrianTranslator()
    unknown = Translator()

    sumerian.next_translator = hurrian
    hurrian.next_translator = unknown

    return sumerian


def run():
    sumerian_text = 'sumerian ala bala'
    hurrian_text = 'hurrian tralala'
    unknown_text = 'this is unknonw'
    translator = _get_translator()
    print(translator.translate(sumerian_text))
    print(translator.translate(hurrian_text))
    print(translator.translate(unknown_text))


if __name__ == '__main__':
    run()
