def select_words(s, filename):
    file_in = open(filename, 'r')
    result = []
    for line in file_in:
        word = line.strip()
        if s in word:
            result.append(word)
    file_in.close()
    return result
