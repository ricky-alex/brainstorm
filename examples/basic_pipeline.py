"""Basic pipeline example."""

from brainstorm import Engine, Pipeline, Module


class TextPreprocessor(Module):
    def __init__(self):
        super().__init__("preprocessor")
    def forward(self, text):
        return text.strip().lower()


class SentimentClassifier(Module):
    def __init__(self):
        super().__init__("classifier")
    def forward(self, text):
        positive = {"good", "great", "amazing", "excellent", "love"}
        words = set(text.split())
        score = len(words & positive) / max(len(words), 1)
        return {"sentiment": "positive" if score > 0.1 else "negative", "confidence": round(score, 3)}


def main():
    pipeline = Pipeline("sentiment")
    pipeline.add(TextPreprocessor())
    pipeline.add(SentimentClassifier())
    engine = Engine()
    result = engine.execute(pipeline, "This is a great and amazing framework!")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
