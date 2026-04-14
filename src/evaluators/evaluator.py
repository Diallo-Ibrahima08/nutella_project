from collections import Counter
import math


def ngrams(tokens, n):
    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]


def bleu_score(references, hypotheses):
    scores = []
    for ref, hyp in zip(references, hypotheses):
        ref_tokens = ref.lower().split()
        hyp_tokens = hyp.lower().split()
        if not hyp_tokens:
            scores.append(0.0)
            continue
        # Bigram precision
        ref_ngrams = Counter(ngrams(ref_tokens, 2))
        hyp_ngrams = Counter(ngrams(hyp_tokens, 2))
        matches = sum((hyp_ngrams & ref_ngrams).values())
        total = sum(hyp_ngrams.values())
        precision = matches / total if total > 0 else 0
        # Brevity penalty
        bp = (
            min(1.0, math.exp(1 - len(ref_tokens) / len(hyp_tokens)))
            if hyp_tokens
            else 0
        )
        scores.append(bp * precision * 100)
    return sum(scores) / len(scores) if scores else 0.0


class Evaluator:
    def __init__(self, df):
        self.df = df

    def evaluate(self):
        references = (
            self.df["reference"].tolist() if "reference" in self.df.columns else []
        )
        hypotheses = (
            self.df["translation"].tolist() if "translation" in self.df.columns else []
        )
        if not references or not hypotheses:
            return {"BLEU": 0.0}
        score = bleu_score(references, hypotheses)
        return {"BLEU": score}
