"""Worst Pizza Topping entry for make.fun.

Writes one funny line pitching a terrible pizza topping to /output/entry.txt.
"""

SETUP = "Introducing toothpaste-and-orange-juice pizza: minty, acidic, "

PUNCH = "and guaranteed to ruin breakfast, lunch, and your will to live."


def assemble():
    return SETUP + PUNCH


LINE = assemble()


def validate(text):
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    line = validate(LINE)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
