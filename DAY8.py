def reverse_words(s: str) -> str:
    # Split string into words, remove extra spaces
    words = s.strip().split()
    # Reverse word list and join with single space
    return " ".join(words[::-1])

s = "the sky is blue"
print(reverse_words(s))   # Output: "blue is sky the"

print(reverse_words("  hello   world  "))  # Output: "world hello"
print(reverse_words("a good   example"))   # Output: "example good a"
