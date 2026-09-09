def correct_sentence(sentence: str):
    sentence = sentence.strip()
    sentence = sentence[0].upper() + sentence[1:]
    return sentence if sentence[-1] == '.' else sentence + "."