class BaseLoader:
    def __init__(self):
        pass

    def load(self):
        raise NotImplementedError("load() must be implemented in subclasses.")
