"""Model serving example."""

from brainstorm import Module
from brainstorm.serving import ModelServer


class MyModel(Module):
    def __init__(self):
        super().__init__("my-model")
    def forward(self, data):
        return {"prediction": 42, "input": data}


def main():
    model = MyModel()
    server = ModelServer(model, port=8080)
    result = server.predict({"text": "hello"})
    print(f"Prediction: {result}")
    print(f"Health: {server.health()}")


if __name__ == "__main__":
    main()
