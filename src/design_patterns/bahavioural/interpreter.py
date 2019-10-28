"""
For validating expressions.
Can be used to evaluate more complex things like:
    - AND
        - EX1
        - EX2
        - OR
            - EX3
            - EX4
"""
import abc
import re


class Expression(abc.ABC):

    @abc.abstractmethod
    def interpret(self, text):
        """
        :return boolean
        """
        return None


class IsLongSentence(Expression):

    def __init__(self, limit):
        self.limit = limit

    def interpret(self, text):
        return isinstance(text, str) and len(text) > self.limit


class IsAboutOrcs(Expression):

    def __init__(self):
        self.regex = re.compile(r'\borcs?\b', re.IGNORECASE)

    def interpret(self, text):
        return isinstance(text, str) and self.regex.search(text)


class OrExpression(Expression):

    def __init__(self, expressions):
        self.expressions = expressions

    def interpret(self, text):
        for expression in self.expressions or []:
            if expression.interpret(text):
                return True

        return False


class AndExpression(Expression):

    def __init__(self, expressions):
        self.expressions = expressions

    def interpret(self, text):
        for expression in self.expressions or []:
            if not expression.interpret(text):
                return False

        return True


def run():
    long_sentence = IsLongSentence(10)
    is_about_orcs = IsAboutOrcs()
    expressions = [long_sentence, is_about_orcs]
    is_long_sentence_OR_is_about_orcs = OrExpression(expressions)
    is_long_sentence_AND_is_about_orcs = AndExpression(expressions)
    s_orcs = 'The orcs are coming !!!'
    s_banana = 'Once upon a time a banana'
    print(is_long_sentence_OR_is_about_orcs.interpret(s_orcs))
    print(is_long_sentence_OR_is_about_orcs.interpret(s_banana))
    print(is_long_sentence_AND_is_about_orcs.interpret(s_orcs))
    print(is_long_sentence_AND_is_about_orcs.interpret(s_banana))


if __name__ == '__main__':
    run()
