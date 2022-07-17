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


def split_into_tokens(phrase):
    lower_case_phrase = phrase.lower()
    tokens = tokenizer(lower_case_phrase, language="portuguese")
    clean_tokens = [apply_stemmer(token) for token in tokens if is_valid_token(token)]
    return clean_tokens


def make_corpus(phrases):
    tokenized_corpus = []
    for phrase in phrases:
        tokenized_phrase = split_into_tokens(phrase=phrase)
        tokenized_corpus.append((phrase, tokenized_phrase))
    return tokenized_corpus


def associate_cluster_per_phrase(phrases, similarity_threshold=95):
    """
    Associates a cluster for each phrase.

    A cluster is representing by a positive integer.

    If a phrase doesn't look like any other, it will receive the value -1.

    Parameters
    ----------
    phrases : list
        A list of strings (phrases).
    similarity_threshold : int
        A integer between 0 and 100.

    Returns
    -------
    list
        A list of size two tuples, where the first item of the tuple is
        the original phrase and the second item is a integer representing
        the cluster's phrase.

    Raises
    ======
     MyException
        if anything bad happens

    See Also
    --------
    group_by_clusters : Subtract one integer from another.

    Examples
    --------
    >>> associate_cluster_per_phrase(["morava em florianópolis", "comprar um carro", "compra de um carro", "em florianópolis eu moro", "gosto de samba", "quero comer tapioca"])
    [('morava em florianópolis', 1), ('comprar um carro', 2), ('compra de um carro', 2), ('em florianópolis eu moro', 1), ('gosto de samba', -1), ('quero comer tapioca', -1)]
    """
    tokenized_corpus = make_corpus(phrases)
    has_cluster = []
    clusters = [(phrase, -1) for phrase in phrases]
    cluster_id = 0
    for i, i_item in enumerate(tokenized_corpus):
        if i_item not in has_cluster:
            new_idx = True
            for j, j_item in enumerate(tokenized_corpus):
                if i != j and j_item[1] not in has_cluster:
                    similarity = fuzz.token_sort_ratio(i_item[1], j_item[1])
                    if similarity >= similarity_threshold:
                        if new_idx:
                            cluster_id += 1
                            clusters[i] = (i_item[0], cluster_id)
                            has_cluster.append(i_item[1])
                            new_idx = False
                        clusters[j] = (j_item[0], cluster_id)
                        has_cluster.append(j_item[1])
    return clusters


# phrases = ["morava em florianópolis", "comprar um carro", "compra de um carro", "moro em florianópolis"]
# res = associate_cluster_per_phrase(phrases)
# print(res)
