from nltk.stem import SnowballStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords
from fuzzywuzzy import fuzz


def set_language(language):
    if language not in SnowballStemmer.languages:
        raise ValueError(f"{language} language is not supported by SnowballStemmer.")
    else:
        global stemmer
        global stops
        global lang
        stemmer = SnowballStemmer(language)
        stops = stopwords.words(language)
        lang = language


def set_simlarity_method(method):
    if method == "token_sort_ratio":
        return fuzz.token_sort_ratio
    elif method == "partial_ratio":
        return fuzz.partial_ratio
    elif method == "token_set_ratio":
        return fuzz.token_set_ratio
    elif method == "ratio":
        return fuzz.ratio


def clean_string(text):
    new_text = "".join([s for s in text if s == " " or s.isalpha()])
    return new_text


def is_valid_token(token):
    is_valid = False
    if token not in stops:
        is_valid = True
    return is_valid


def split_into_tokens(sentence):
    lower_case_sentence = sentence.lower()
    clean_sentence = clean_string(lower_case_sentence)
    tokens = word_tokenize(clean_sentence, language=lang)
    clean_tokens = [stemmer.stem(token) for token in tokens if is_valid_token(token)]
    return clean_tokens


def make_corpus(sentences):
    tokenized_corpus = []
    for sentence in sentences:
        tokenized_sentence = split_into_tokens(sentence=sentence)
        tokenized_corpus.append(tokenized_sentence)
    return tokenized_corpus


def look_for_clusters(
    sentences, language="english", method="token_sort_ratio", similarity_threshold=95
):
    """
    Associates a cluster for each sentence.

    A cluster is representing by a positive integer.

    If a sentence doesn't look like any other, it will receive the value -1.

    Parameters
    ----------
    sentences: list
        A list of strings (sentences).
    language: string
        The language to use.
    method: string
        The method for measuring similarity.
    similarity_threshold: int
        A integer between 0 and 100. Default value is 95.

    Returns
    -------
    list
        A list of integers representing clusters.

    Raises
    ======

    Examples
    --------
    >>> sentences = [
        "I live in New York",
        "I want to buy a car",
        "a car I would like to buy",
        "Ohh New York, I lived there in 2005",
        "I have a dog",
    ]
    >>> look_for_clusters(sentences, 60)
    output: [1, 2, 2, 1, -1]
    """
    set_language(language)
    similarity_method = set_simlarity_method(method=method)
    clusters = [-1] * len(sentences)
    tokenized_corpus = make_corpus(sentences)
    clean_sentences = [" ".join(tokenized_doc) for tokenized_doc in tokenized_corpus]
    cluster_id = 0
    for i, i_item in enumerate(clean_sentences):
        if i_item != "":
            for j, j_item in enumerate(clean_sentences[i:]):
                j += i
                if i != j and j_item != "" and clusters[j] < 0:
                    similarity = similarity_method(i_item, j_item)
                    if similarity >= similarity_threshold:
                        if clusters[i] < 0:
                            cluster_id += 1
                            clusters[i] = cluster_id
                            clusters[j] = cluster_id
                        else:
                            clusters[j] = clusters[i]
    return clusters


if __name__ == "__main__":
    eng_sentences = [
        "I live in New York",
        "I want to buy a car",
        "a car I would like to buy",
        "Ohh New York, I lived there in 2005",
        "I have a dog",
    ]
    ger_sentences = [
        "ich lebe in New York",
        "Ich möchte ein Auto kaufen",
        "ein Auto, das ich kaufen möchte",
        "Oh New York, Ich habe dort 2005 gelebt",
        "Ich habe einen Hund",
    ]
    eng_res = look_for_clusters(eng_sentences, similarity_threshold=60)
    ger_res = look_for_clusters(
        ger_sentences,
        language="german",
        method="token_set_ratio",
        similarity_threshold=80,
    )
    print(eng_res)
    print(ger_res)
