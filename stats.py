def get_num_words(book):
    words = book.split()
    return len(words)

def get_num_char(book):
    result = {}
    for c in book:
        key = c.lower()
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result