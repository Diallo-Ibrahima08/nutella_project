class BaseEvaluator:
    def __init__(self):
        pass

    def evaluate(self, data):
        raise NotImplementedError("evaluate() must be implemented in subclasses.")
