import string


def clean_text(text):
    """
    Removes punctuation and converts text to lowercase.
    """
    text = text.lower()

    for mark in string.punctuation:
        text = text.replace(mark, "")

    return text


def count_specific_word(text, word):
    """
    Counts how many times a specific word appears.
    Uses a while loop as required.
    """

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
    """
    Returns the most common word.
    Returns None if the text is empty.
    """

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
    """
    Calculates the average word length.
    Returns 0 for an empty string.
    """

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
    """
    Counts paragraphs separated by blank lines.
    Returns 1 for an empty string.
    """

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
    """
    Counts sentences ending with ., ! or ?
    Returns 1 for an empty string.
    """

    if text == "":
        return 1

    count = 0

    for character in text:

        if character == "." or character == "!" or character == "?":
            count += 1

    return count
