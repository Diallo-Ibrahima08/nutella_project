class BaseProcessor:
    def __init__(self):
        pass

    def process(self, data):
        raise NotImplementedError("process() must be implemented in subclasses.")
