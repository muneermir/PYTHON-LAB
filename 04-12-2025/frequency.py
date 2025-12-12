from collections import defaultdict
def word_frequency(filename):
    freq = defaultdict(int)
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                word = ''.join(ch for ch in word if ch.isalnum()).lower()
                if word:
                    freq[word] += 1
    return dict(freq)

# Example (ensure file exists)
print(word_frequency("Muneer.txt"))
