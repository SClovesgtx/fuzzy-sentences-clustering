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


def clean_token(token):
    new_token = "".join([s for s in token if s.isalpha()])
    return new_token


def is_valid_token(token):
    is_valid = False
    if token not in stopwords:
        is_valid = True
    return is_valid


def apply_stemmer(token):
    new_token = clean_token(token=token)
    if new_token:
        return stemmer.stem(new_token)
    return ""


def split_into_tokens(sentence):
    lower_case_sentence = sentence.lower()
    tokens = tokenizer(lower_case_sentence, language="portuguese")
    clean_tokens = [apply_stemmer(token) for token in tokens if is_valid_token(token)]
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
     MyException
        if anything bad happens

    Examples
    --------
    >>> look_for_clusters(["morava em florianópolis", "comprar um carro", "compra de um carro", "em florianópolis eu moro", "gosto de samba", "quero comer tapioca"])
    [('morava em florianópolis', 1), ('comprar um carro', 2), ('compra de um carro', 2), ('em florianópolis eu moro', 1), ('gosto de samba', -1), ('quero comer tapioca', -1)]
    """
    tokenized_corpus = make_corpus(sentences)
    has_cluster = []
    clusters = [-1] * len(sentences)
    cluster_id = 0
    for i, i_item in enumerate(tokenized_corpus):
        if i_item not in has_cluster:
            new_idx = True
            for j, j_item in enumerate(tokenized_corpus):
                if i != j and j_item not in has_cluster:
                    similarity = fuzz.token_sort_ratio(i_item, j_item)
                    if similarity >= similarity_threshold:
                        if new_idx:
                            cluster_id += 1
                            clusters[i] = cluster_id
                            has_cluster.append(i_item)
                            new_idx = False
                        clusters[j] = cluster_id
                        has_cluster.append(j_item)
    return clusters


if __name__ == "__main__":
    sentences = [
        "morava em florianópolis",
        "comprar um carro",
        "compra de um carro",
        "em florianópolis eu moro",
        "gosto de samba",
        "quero comer tapioca",
    ]
    res = look_for_clusters(sentences)
    print(res)
