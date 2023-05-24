import pytest
from main import word_frequency

test_data = [
    pytest.param(
        [
            "Hello,",
            "hello,",
            "HELLO!"
        ],
        {
            "hello": 3
        },
        id="case_insensitive"
    ),
    pytest.param(
        [
            "The quick brown fox",
            "jumps over the lazy dog.",
            "The dog barks,",
            "and the fox runs away."
        ],
        {
            "the": 4,
            "quick": 1,
            "brown": 1,
            "fox": 2,
            "jumps": 1,
            "over": 1,
            "lazy": 1,
            "dog": 2,
            "barks": 1,
            "and": 1,
            "runs": 1,
            "away": 1
        },
        id="multiple_words"
    ),
    pytest.param(
        [
            "Multiple words",
            "in one line",
            "separated by spaces"
        ],
        {
            "multiple": 1,
            "words": 1,
            "in": 1,
            "one": 1,
            "line": 1,
            "separated": 1,
            "by": 1,
            "spaces": 1
        },
        id="multiple_lines"
    ),
    pytest.param(
        [
            "Apple",
            "apple",
            "apple.",
            "apple,"
        ],
        {
            "apple": 4
        },
        id="punctuation"
    ),
    pytest.param(
        [
            "  leading whitespace",
            "trailing whitespace   ",
            "  leading and trailing whitespace  "
        ],
        {
            "leading": 2,
            "whitespace": 3,
            "trailing": 2,
            "and": 1
        },
        id="whitespace"
    ),
    pytest.param(
        [
            "Punctuation marks!",
            "attached to words?",
            "should be excluded.",
            "punctuation marks."
        ],
        {
            "punctuation": 2,
            "marks": 2,
            "attached": 1,
            "to": 1,
            "words": 1,
            "should": 1,
            "be": 1,
            "excluded": 1
        },
        id="punctuation_marks"
    ),
    pytest.param(
        [
            "Empty string",
            "",
            "excluded as word"
        ],
        {
            "empty": 1,
            "string": 1,
            "excluded": 1,
            "as": 1,
            "word": 1
        },
        id="empty_string"
    ),
    pytest.param(
        [],
        {},
        id="empty_input"
    )
]


@pytest.mark.parametrize("paragraph, expected_result", test_data)
def test_word_frequency(paragraph, expected_result):
    assert word_frequency(paragraph) == expected_result