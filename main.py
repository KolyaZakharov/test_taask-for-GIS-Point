def word_frequency(paragraph: list) -> dict:
    result = {}
    for string in paragraph:
        words = string.strip(".,!:;?").lower().split()
        for word in words:
            result[word] = result.get(word, 0) + 1
    return result


paragraph = [
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away."
]

frequency = word_frequency(paragraph)
print(frequency)
