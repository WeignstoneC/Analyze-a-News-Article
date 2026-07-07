import string


def clean_text(text):
    """Remove punctuation and lowercase text."""
    text = text.lower()
    for mark in string.punctuation:
        text = text.replace(mark, "")
    return text


def count_specific_word(text, word):
    """Count occurrences of a word in text."""
    if text == "" or word == "":
        return 0
    text = clean_text(text)
    words = text.split()
    count = 0
    index = 0
    while index < len(words):
        if words[index] == word.lower():
            count += 1
        index += 1
    return count


def identify_most_common_word(text):
    """Return the most common word or None if empty."""
    if text == "":
        return None
    text = clean_text(text)
    words = text.split()
    if len(words) == 0:
        return None
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    most_common = None
    highest = 0
    for word in frequency:
        if frequency[word] > highest:
            highest = frequency[word]
            most_common = word
    return most_common


def calculate_average_word_length(text):
    """Return the average word length as a float."""
    if text == "":
        return 0
    text = clean_text(text)
    words = text.split()
    if len(words) == 0:
        return 0
    total = 0
    for word in words:
        total += len(word)
    average = total / len(words)
    return round(average, 2)


def count_paragraphs(text):
    """Count blocks of text separated by blank lines."""
    if text == "":
        return 1
    else:
        paragraphs = text.split("\n\n")
        count = 0
        for paragraph in paragraphs:
            if paragraph.strip() != "":
                count += 1
        return count


def count_sentences(text):
    """Count sentence-ending punctuation marks."""
    if text == "":
        return 1
    count = 0
    for character in text:
        if character == "." or character == "!" or character == "?":
            count += 1
    return count
