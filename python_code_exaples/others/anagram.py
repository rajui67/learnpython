from collections import Counter

def is_anagram(first: str, second: str) -> bool:
    return Counter(first) == Counter(second)

is_anagram('abcd', 'dbac')

