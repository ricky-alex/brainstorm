"""Custom transform example."""

from brainstorm.transforms.base import Transform


class Uppercase(Transform):
    """Transform text to uppercase."""

    def __call__(self, data):
        return data.upper() if isinstance(data, str) else data


class Trim(Transform):
    """Trim whitespace."""

    def __call__(self, data):
        return data.strip() if isinstance(data, str) else data


def main():
    upper = Uppercase()
    trim = Trim()

    text = "  Hello Brainstorm  "
    print(f"Original: '{text}'")
    print(f"Upper: '{upper(text)}'")
    print(f"Trim: '{trim(text)}'")


if __name__ == "__main__":
    main()
