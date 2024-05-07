from itertools import permutations
from time import time
import nltk

nltk.download("words")

from nltk.corpus import words


def find_words(letters: str, min_length: int = 4, max_time: int = 5) -> set[str]:
    start_time: float = time()
    valid_words: set[str] = set(words.words())
    found_words: set[str] = set()

    for i in range(min_length, len(letters) + 1):
        for perm in permutations(letters, i):
            if time() - start_time > max_time:

                if not found_words:
                    raise Exception("No words found")

                return found_words

            word = "".join(perm).lower()

            if word in valid_words:
                found_words.add(word)

    if not found_words:
        raise Exception("No words found")

    return found_words
