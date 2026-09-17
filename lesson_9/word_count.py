def popular_words (text :str , words: list) -> dict[str, int]:
    word_count = { _ : 0 for _ in words}
    text_words = text.lower().split()
    for word in words:
        word_count[word] += text_words.count(word.lower())
    return word_count

