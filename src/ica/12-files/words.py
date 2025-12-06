def i_words(filename):
    file_in = open(filename, 'r')
    text = file_in.read()
    file_in.close()

    words = text.split()
    result = []
    for w in words:
        if 'i' in w:
            result.append(w)
    return result
