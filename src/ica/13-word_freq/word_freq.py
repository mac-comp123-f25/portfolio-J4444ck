import string

def compute_frequencies(filename):
    with open(filename, 'r') as file:
        text = file.read()

    words = text.split()
    cleaned_words = []
    for word in words:
        cleaned = word.strip(string.punctuation).lower()
        if cleaned != '':
            cleaned_words.append(cleaned)

    freq = {}
    for word in cleaned_words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


if __name__ == "__main__":
    filename = input("Enter filename: ")
    frequencies = compute_frequencies(filename)
    print(frequencies)