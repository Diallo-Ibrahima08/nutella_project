class BaseTranslator:
    def __init__(self):
        pass

    def translate(self, data):
        raise NotImplementedError("translate() must be implemented in subclasses.")
