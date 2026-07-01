import re


def count_specific_word(text: str, search_word: str) -> int:
    if not text or not search_word:
        return 0

    normalized_text = re.sub(r"[^A-Za-z0-9']+", ' ', text).lower()
    normalized_search_word = search_word.lower()
    words = normalized_text.split()
    count = 0
    for word in words:
        if word == normalized_search_word:
            count += 1
    return count


def identify_most_common_word(text: str) -> str | None:
    if not text:
        return None

    normalized_text = re.sub(r"[^A-Za-z0-9']+", ' ', text).lower()
    words = [word for word in normalized_text.split() if word]
    if not words:
        return None

    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    most_common = max(frequency.items(), key=lambda item: item[1])
    return most_common[0]


def calculate_average_word_length(text: str) -> float:
    if not text:
        return 0.0

    normalized_text = re.sub(r"[^A-Za-z0-9']+", ' ', text)
    words = [word for word in normalized_text.split() if word]
    if not words:
        return 0.0

    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
    return average_length


def count_paragraphs(text: str) -> int:
    if text == '':
        return 1

    paragraphs = [paragraph for paragraph in text.split('\n\n') if paragraph.strip()]
    return len(paragraphs) if paragraphs else 1


def count_sentences(text: str) -> int:
    if text == '':
        return 1

    sentences = re.split(r"[.!?]+\s*", text.strip())
    sentences = [sentence for sentence in sentences if sentence]
    return len(sentences) if sentences else 1


def display_analysis(text: str) -> None:
    print('Text Analysis Results')
    print('---------------------')
    print(f"Number of paragraphs: {count_paragraphs(text)}")
    print(f"Number of sentences: {count_sentences(text)}")
    print(f"Most common word: {identify_most_common_word(text)}")
    print(f"Average word length: {calculate_average_word_length(text):.2f}")

    sample_word = 'apple'
    print(f"Count of '{sample_word}': {count_specific_word(text, sample_word)}")


def main() -> None:
    article_path = 'news_article.txt'

    try:
        with open(article_path, 'r', encoding='utf-8') as file:
            article_text = file.read()
    except FileNotFoundError:
        print(f'Error: Could not open {article_path}.')
        return

    display_analysis(article_text)

    additional_searches = [
        ('machine', article_text),
        ('pie', article_text),
        ('automation', article_text),
    ]

    index = 0
    while index < len(additional_searches):
        search_word, text = additional_searches[index]
        count = count_specific_word(text, search_word)
        print(f"The word '{search_word}' appears {count} time(s) in the article.")
        index += 1

    for word in ['technology', 'baking', 'sustainability']:
        if count_specific_word(article_text, word) > 0:
            print(f"The article mentions '{word}'.")
        else:
            print(f"The article does not mention '{word}'.")


if __name__ == '__main__':
    main()
