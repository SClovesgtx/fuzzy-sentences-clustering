import nltk
from fuzzywuzzy import fuzz

try:
    stemmer = nltk.stem.RSLPStemmer()
    stopwords = nltk.corpus.stopwords.words("portuguese")
    tokenizer = nltk.tokenize.word_tokenize
except:
    nltk.download("rslp")
    nltk.download("stopwords")
    nltk.download("punkt")
    stemmer = nltk.stem.RSLPStemmer()
    stopwords = nltk.corpus.stopwords.words("portuguese")
    tokenizer = nltk.tokenize.word_tokenize


def clean_string(text):
    new_text = "".join([s for s in text if s == " " or s.isalpha()])
    return new_text


def is_valid_token(token):
    is_valid = False
    if token not in stopwords:
        is_valid = True
    return is_valid

def split_into_tokens(sentence):
    lower_case_sentence = sentence.lower()
    clean_sentence = clean_string(lower_case_sentence)
    tokens = tokenizer(clean_sentence, language="portuguese")
    clean_tokens = [stemmer.stem(token) for token in tokens if is_valid_token(token)]
    return clean_tokens


def make_corpus(sentences):
    tokenized_corpus = []
    for sentence in sentences:
        tokenized_sentence = split_into_tokens(sentence=sentence)
        tokenized_corpus.append(tokenized_sentence)
    return tokenized_corpus


def look_for_clusters(sentences, similarity_threshold=95):
    """
    Associates a cluster for each sentence.

    A cluster is representing by a positive integer.

    If a sentence doesn't look like any other, it will receive the value -1.

    Parameters
    ----------
    sentences : list
        A list of strings (sentences).
    similarity_threshold : int
        A integer between 0 and 100.

    Returns
    -------
    list
        A list of integers representing clusters.

    Raises
    ======

    Examples
    --------
    >>> look_for_clusters(["morava em florianópolis", "comprar um carro", "compra de um carro", "em florianópolis eu moro", "gosto de samba", "quero comer tapioca"])
    output: [1, 2, 2, 1, -1, -1]
    """
    clusters = [-1] * len(sentences)
    tokenized_corpus = make_corpus(sentences)
    clean_sentences = [" ".join(tokenized_doc) for tokenized_doc in tokenized_corpus]
    cluster_id = 0
    for i, i_item in enumerate(clean_sentences):
        if i_item != "":
            for j, j_item in enumerate(clean_sentences):
                if i != j:
                    similarity = fuzz.token_sort_ratio(i_item, j_item)
                    if similarity >= similarity_threshold:
                        if clusters[i] < 0:
                            cluster_id += 1
                            clusters[i] = cluster_id
                            clusters[j] = cluster_id
                        elif clusters[i] > 0:
                            clusters[j] = clusters[i]
    return clusters


if __name__ == "__main__":
    sentences = [
        "morava em florianópolis",
        "comprar um carro",
        "compra de um carro",
        "em florianópolis eu moro",
    ]
    res = look_for_clusters(sentences, 50)
    print(res)
