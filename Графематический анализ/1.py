import nltk
import string

nltk.download("punkt")

with open(
    "C:\\Users\\user\\Desktop\\python\\Графематический анализ\\1.txt", encoding="utf-8"
) as file:
    text = file.read()
    tokens = nltk.word_tokenize(text)
    remove_punctuation = str.maketrans("", "", string.punctuation)
    tokens_ = [
        x
        for x in [t.translate(remove_punctuation).lower() for t in tokens]
        if len(x) > 0
    ]
    text2 = nltk.Text(tokens_)
    lexical_diversity = (len(set(text2)) / len(text2)) * 100
    print(f"Лексическое разнообразие книги: {lexical_diversity}%")
