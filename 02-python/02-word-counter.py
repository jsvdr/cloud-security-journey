OPTIONS = {"words", "chars", "lines"}


def analyze_text(text: str, mode: str) -> int | str:
    if mode == "words":
        return len(text.split())
    if mode == "chars":
        return len(text)
    if mode == "lines":
        return len(text.splitlines())
    return "Invalid mode"


def main() -> None:
    """Read stdin, validate option, print count."""
    text = input("Enter text to analyze: ")

    mode = input("Enter mode (words, chars, lines): ").strip().lower()
    if mode not in OPTIONS:
        print("Invalid mode.")
        return

    result = analyze_text(text, mode)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
